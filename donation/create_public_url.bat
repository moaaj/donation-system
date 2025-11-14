@echo off
echo 🌐 Creating Public URL for Client Demo...
echo.

REM Check if Docker is running
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker is not installed or running
    echo Please install Docker Desktop from: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

echo 📦 Starting Django app with Docker...
docker-compose -f docker-compose.local.yml up --build -d

echo ⏳ Waiting for app to start (15 seconds)...
timeout /t 15 /nobreak

echo 🔍 Checking if app is running...
curl -s http://localhost:8000 >nul 2>&1
if errorlevel 1 (
    echo ⚠️ App might still be starting. Check http://localhost:8000 manually
) else (
    echo ✅ App is running at http://localhost:8000
)

echo.
echo 🌐 CREATING PUBLIC URL...
echo.

REM Check if ngrok is installed
ngrok version >nul 2>&1
if errorlevel 1 (
    echo 📥 Ngrok not found. Please:
    echo 1. Go to: https://ngrok.com/download
    echo 2. Download ngrok for Windows
    echo 3. Extract to a folder in your PATH
    echo 4. Sign up at https://ngrok.com for free
    echo 5. Run: ngrok config add-authtoken YOUR_TOKEN
    echo 6. Then run this script again
    echo.
    pause
    exit /b 1
)

echo 🚀 Starting ngrok tunnel...
echo ⚠️ Keep this window open! Closing it will stop the public URL.
echo.
echo 🔗 Your public URL will appear below:
echo 📋 Share this URL with your clients for instant demo access!
echo.

REM Start ngrok (this will run in foreground)
ngrok http 8000
