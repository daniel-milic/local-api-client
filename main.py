from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import httpx
from typing import Optional, Dict, Any
import json
from collections import defaultdict
import time
from pathlib import Path

app = FastAPI(
    title="REST Client Proxy",
    description="Simple proxy backend for browser-based REST client",
    version="1.0"
)

# Very permissive CORS for local dev – tighten in production!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>index.html not found in current directory</h1>"

# ── Domain whitelist ────────────────────────────────────────────────────────
ALLOWED_DOMAINS_FILE = Path("whitelist.json")

try:
    with ALLOWED_DOMAINS_FILE.open("r") as f:
        allowed_domains = json.load(f)
    print(f"Loaded allowed domains: {len(allowed_domains)} entries")
except Exception as e:
    print(f"Warning: Could not load allowed_domains.json → {e}")
    allowed_domains = []  # block everything if file missing/broken

def is_allowed_url(url: str) -> bool:
    if not allowed_domains:
        return False
    try:
        from urllib.parse import urlparse
        domain = urlparse(url).hostname.lower()
        for allowed in allowed_domains:
            allowed = allowed.lower()
            if allowed.startswith("*."):
                suffix = allowed[2:]
                if domain == suffix or domain.endswith("." + suffix):
                    return True
            elif allowed == domain or domain.endswith("." + allowed):
                return True
        return False
    except:
        return False

# ── Simple in-memory rate limiter (sliding window, per IP) ──────────────────
# 6 requests per 60 seconds per IP — adjust as needed
RATE_LIMIT = 120
RATE_WINDOW = 60  # seconds

request_history: Dict[str, list[float]] = defaultdict(list)

def is_rate_limited(client_ip: str) -> bool:
    now = time.time()
    history = request_history[client_ip]
    
    # Remove old requests
    history[:] = [t for t in history if now - t < RATE_WINDOW]
    
    if len(history) >= RATE_LIMIT:
        return True
    
    history.append(now)
    return False

# ── Proxy endpoint ──────────────────────────────────────────────────────────
class ProxyRequest(BaseModel):
    method: str
    url: str
    headers: Optional[Dict[str, str]] = None
    body: Optional[Any] = None

@app.post("/proxy")
async def proxy_request(req: ProxyRequest, request: Request):
    client_ip = request.client.host
    if is_rate_limited(client_ip):
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded (30 req / 60s) — slow down"
        )

    if not is_allowed_url(req.url):
        raise HTTPException(
            status_code=403,
            detail="Target domain not allowed by server configuration - update whitelist.json"
        )

    method = req.method.upper()
    if method not in {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}:
        raise HTTPException(400, detail="Unsupported HTTP method")

    headers = req.headers or {}
    forbidden = {
        "host", "connection", "keep-alive", "proxy-authenticate",
        "proxy-authorization", "te", "trailers", "transfer-encoding", "upgrade"
    }
    clean_headers = {k: v for k, v in headers.items() if k.lower() not in forbidden}

    async with httpx.AsyncClient(follow_redirects=True, timeout=30.0) as client:
        try:
            resp = await client.request(
                method=method,
                url=req.url,
                headers=clean_headers,
                content=req.body if isinstance(req.body, (str, bytes)) else None,
                json=req.body if isinstance(req.body, (dict, list)) else None,
            )

            response_headers = dict(resp.headers)
            for h in ["content-encoding", "transfer-encoding", "content-length"]:
                response_headers.pop(h, None)

            return {
                "status": resp.status_code,
                "status_text": resp.reason_phrase or "",
                "headers": response_headers,
                "body": resp.text,
                "ok": resp.is_success,
            }

        except httpx.TimeoutException:
            raise HTTPException(504, "Gateway Timeout")
        except httpx.RequestError as e:
            raise HTTPException(502, f"Proxy request failed: {str(e)}")
        except Exception as e:
            raise HTTPException(500, f"Internal error: {str(e)}")