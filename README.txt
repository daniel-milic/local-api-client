Local API Client

Simple browser-based API client that runs 100% locally
Frontend ↔ FastAPI proxy (no CORS headaches)


Setup – Use a virtual environment (recommended for all platforms)
----------------------------------------------------------------

This keeps your system Python clean and avoids permission / conflict issues.

1. Open a terminal / command prompt in your project folder

2. Create virtual environment
   python -m venv .venv
   (or python3 -m venv .venv on some Linux/macOS systems)

3. Activate it

   Windows (Command Prompt or PowerShell):
      .venv\Scripts\activate

   macOS / Linux / Git Bash:
      source .venv/bin/activate

   → You should see (.venv) appear in your prompt

4. Install packages
   pip install fastapi uvicorn httpx pydantic

   (or exact versions if you prefer:)
   pip install fastapi==0.115.2 uvicorn==0.30.6 httpx==0.27.2 pydantic==2.9.2

5. (Important) Edit whitelist.json before starting the server
   ---------------------------------------------------------
   The proxy only allows requests to domains listed in whitelist.json.

   Example:

   [
       "api.github.com",
       "httpbin.org",
       "localhost",
       "127.0.0.1",
       "jsonplaceholder.typicode.com",
       "your-api.example.com"
   ]

   • Add the domains you plan to use
   • Supports wildcards like "*.example.com"
   • Changes take effect after server restart

6. Start the server
   uvicorn main:app --reload --port 8000

7. Open in browser:
   http://localhost:8000/


Alternative: using requirements.txt
-----------------------------------

After activating the virtual environment:
   pip install -r requirements.txt


When finished:
   deactivate


Features
--------

- GET / POST / PUT / PATCH / DELETE
- Custom headers (one per line: Key: Value)
- Request body (JSON friendly)
- Pretty-printed JSON response
- History saved in browser (localStorage)
- Filter, delete, export/import history
- Enter in URL/headers/body field = Send


VERY IMPORTANT SECURITY WARNING
-------------------------------

THIS TOOL IS NOT INTENDED FOR PUBLIC OR SHARED USE

Even with domain whitelisting and basic rate limiting:
- Rate limiting is minimal (in-memory, per IP only, resets on restart)
- It can be easily bypassed (multiple IPs, short bursts, etc.)
- No authentication, no advanced abuse protection

DO NOT expose this on the public internet, even temporarily.
Doing so can lead to:
- Denial-of-service attacks against your server
- Your IP being used for outbound abuse / scraping / attacks
- Hosting provider complaints / suspension
- Unexpected high bandwidth / CPU usage

Keep it strictly for **personal, local development use only** (localhost or your private machine).

For anything shared or production-related, use established tools:
Postman, Insomnia, Bruno, Thunder Client, Hoppscotch desktop, curl/wget scripts, etc.

Enjoy local API testing!

Vibe-coded together with Grok • xAI