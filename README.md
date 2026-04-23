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

## Screenshots

### Main interface with Test Runner + Donut Chart + Response Times

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

*   Frontend: single-file HTML + CSS + vanilla JavaScript (with Test Runner, ECharts donut chart, and response timing)
*   Backend: FastAPI + httpx
*   History & test status: browser localStorage

---

Enjoy testing and **validating** your APIs locally!

Vibe-coded together with Grok • xAI
```

**✅ README updated!**

The new version now prominently highlights:

- **Response time (ms)** in the history list
- **Multi-word space-separated search** (AND logic with smart `pass`/`fail` handling)
- **Donut pie chart** in the Test Results panel

I also refreshed the "Why use it" and "Tech stack" sections for consistency.

Just replace the content of your `README.md` with the markdown above (or copy-paste the updated sections). Let me know if you'd like a new screenshot caption, a dedicated "How to use the Test Runner" subsection, or any other tweaks!