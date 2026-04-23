@echo off
:: Local API Client - Start Script (Windows)

echo 🚀 Starting Local API Client...
echo =====================================

:: Activate virtual environment if it exists
if exist .venv\Scripts\activate.bat (
    echo ✅ Activating virtual environment (.venv)
    call .venv\Scripts\activate.bat
) else if exist venv\Scripts\activate.bat (
    echo ✅ Activating virtual environment (venv)
    call venv\Scripts\activate.bat
) else (
    echo ⚠️  No virtual environment found. Running with global Python...
)

:: Check if uvicorn is installed
where uvicorn >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ uvicorn not found. Please run: pip install fastapi uvicorn httpx pydantic
    pause
    exit /b 1
)

echo 🌐 Starting uvicorn on http://localhost:8000
echo    (Press Ctrl+C to stop)
echo.

uvicorn main:app --reload --port 8000

pause