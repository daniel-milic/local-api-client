#!/bin/bash
# Local API Client - Start Script (Linux / macOS)

echo "🚀 Starting Local API Client..."
echo "====================================="

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    echo "✅ Activating virtual environment (.venv)"
    source .venv/bin/activate
elif [ -d "venv" ]; then
    echo "✅ Activating virtual environment (venv)"
    source venv/bin/activate
else
    echo "⚠️  No virtual environment found. Running with global Python..."
fi

# Check if uvicorn is installed
if ! command -v uvicorn &> /dev/null; then
    echo "❌ uvicorn not found. Please run: pip install fastapi uvicorn httpx pydantic"
    exit 1
fi

echo "🌐 Starting uvicorn on http://localhost:8000"
echo "   (Press Ctrl+C to stop)"
echo ""

uvicorn main:app --reload --port 8000