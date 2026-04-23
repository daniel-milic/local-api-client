**✅ Done!**  

I’ve updated your `README.md` and added two new **start scripts** for easy launching:

- `start.bat` → Windows  
- `start.sh` → Linux / macOS  

### How to use (new recommended way)

Just double-click `start.bat` (Windows) or run `./start.sh` (Linux/macOS) — the scripts automatically:

- Activate your virtual environment (`.venv` or `venv`)
- Check for uvicorn
- Start the server on `http://localhost:8000`

---

### 📁 Here are the three updated/added files:

**1. Updated `README.md`** (replace your current file with this)

```markdown
# Local API Client

Simple browser-based API client that runs **100% locally**  
Frontend ↔ FastAPI proxy (no CORS issues)

## Why use it?

*   Everything stays on your machine — no cloud service, no tracking
*   Bypasses browser CORS restrictions via a tiny FastAPI proxy
*   Persistent request history saved in the browser (localStorage)
*   **New**: Built-in Test Runner with donut chart + smart multi-word filtering + response timing
*   Very lightweight — single HTML file + minimal Python backend
*   Great lightweight alternative to Postman/Insomnia for quick local testing

## Features

*   GET / POST / PUT / PATCH / DELETE
*   Custom headers (one per line: `Key: Value`)
*   Request body (JSON or text — textarea)
*   Pretty-printed JSON responses + status code / text
*   **History**:
    *   Automatically saves successful requests
    *   **Response time** displayed in milliseconds (`XXX ms`) right before the timestamp
    *   Smart **multi-word search** (space-separated terms) with **AND logic**
    *   Special status keyword handling (`pass fail`, `pass pokeapi`, `GET api success`, etc.)
    *   Save to History toggle (persists in localStorage)
    *   Click any item to reload method, URL, headers, body and response
    *   Show recent / Show all toggle
    *   Delete single items
    *   Import / Export history as JSON (great for backup or sharing)
*   **Test Runner** (New!):
    *   Dedicated **Test Results** sidebar panel
    *   Beautiful **donut pie chart** (ECharts) showing pass/fail distribution with total count in the center
    *   **Run Tests** button executes **only the currently visible** (filtered) requests
    *   Fully respects the active filter — filter first to test a specific subset
    *   Modern status indicators (green ✓ = pass, red ✕ = fail) next to every history item
    *   Automatically updates response, status, timestamp **and response time** on every run
    *   Live progress + final summary with pass/fail counts and donut visualization
*   Keyboard shortcut: **Ctrl + Enter** (or Cmd + Enter on Mac) to send request

## Quick Start (Recommended)

1. Clone or download the repository

   ```bash
   git clone https://github.com/daniel-milic/local-api-client.git
   cd local-api-client
   ```

2. Create and activate virtual environment (once)

   **Windows:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS / Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies (once)

   ```bash
   pip install fastapi uvicorn httpx pydantic
   ```

4. **Important** — edit `whitelist.json` before starting (only domains listed here are allowed through the proxy).

5. **Start the server** using the convenient start script:

   **Windows:** Double-click `start.bat`  
   **Linux / macOS:**
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

   The script will automatically activate the virtual environment and launch uvicorn on `http://localhost:8000`.

6. Open in browser: `http://localhost:8000/`

## Setup (Manual alternative)

If you prefer the manual way, follow the old steps and run:
```bash
uvicorn main:app --reload --port 8000
```

## Security & Usage Notes

**For local / personal development use only.**

*   Proxy is restricted via `whitelist.json`
*   Basic rate limiting included
*   Do not expose publicly

## Tech stack

*   Frontend: single-file HTML + CSS + vanilla JavaScript (with Test Runner, ECharts donut chart, and response timing)
*   Backend: FastAPI + httpx
*   History & test status: browser localStorage

---

Enjoy testing and **validating** your APIs locally!

Vibe-coded together with Grok • xAI

