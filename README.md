# Local API Client

Simple browser-based API client that runs **100% locally**  
Frontend ↔ FastAPI proxy (no CORS issues)

## Why use it?

*   Everything stays on your machine — no cloud service, no tracking
*   Bypasses browser CORS restrictions via a tiny FastAPI proxy
*   Persistent request history saved in the browser (localStorage)
*   **New**: Built-in Test Runner with visual pass/fail indicators
*   Very lightweight — single HTML file + minimal Python backend
*   Great lightweight alternative to Postman/Insomnia for quick local testing

## Features

*   GET / POST / PUT / PATCH / DELETE
*   Custom headers (one per line: `Key: Value`)
*   Request body (JSON or text — textarea)
*   Pretty-printed JSON responses + status code / text
*   **History**:
    *   Automatically saves successful requests
    *   Save to History toggle (persists in localStorage)
    *   Click any item to reload method, URL, headers, body and response
    *   Filter by URL / body / response content
    *   Show recent / Show all toggle
    *   Delete single items
    *   Import / Export history as JSON (great for backup or sharing)
*   **Test Runner** (New!):
    *   Dedicated **Test Results** sidebar panel
    *   **Run Tests** button
    *   Executes **only the currently visible requests** in the History panel
    *   Fully respects the active filter — filter first to test a specific subset
    *   Modern status indicators (green ✓ = pass, red ✕ = fail) next to every history item
    *   Automatically updates response, status, and **timestamp** on every run
    *   Live progress + final pass/fail summary with counts
*   Keyboard shortcut: **Ctrl + Enter** (or Cmd + Enter on Mac) to send request

## Screenshots

### Main interface with Test Runner

![Local API Client with Test Results](screenshots/main.png)

## Setup (recommended: virtual environment)

1. Clone or download the repository

   ```bash
   git clone https://github.com/daniel-milic/local-api-client.git
   cd local-api-client
   ```

2. Create and activate virtual environment

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

3. Install dependencies

   ```bash
   pip install fastapi uvicorn httpx pydantic
   ```

4. **Important** — edit `whitelist.json` before starting

   Only domains listed here are allowed through the proxy.

5. Start the server

   ```bash
   uvicorn main:app --reload --port 8000
   ```

6. Open in browser: `http://localhost:8000/`

## Security & Usage Notes

**For local / personal development use only.**

*   Proxy is restricted via `whitelist.json`
*   Basic rate limiting included
*   Do not expose publicly

## Tech stack

*   Frontend: single-file HTML + CSS + vanilla JavaScript (with Test Runner)
*   Backend: FastAPI + httpx
*   History & test status: browser localStorage

---

Enjoy testing and **validating** your APIs locally!

Vibe-coded together with Grok • xAI
```

**✅ Done!**  
I’ve updated the README.md with a clear, prominent section for the new **Test Runner** feature, including how filtering works, status indicators, timestamp updates, and the sidebar.

Would you like me to also update the screenshot caption or add anything else (e.g. a dedicated “How to use Test Runner” subsection)? Just say the word and I’ll refine it further!