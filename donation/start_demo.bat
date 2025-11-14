@echo off
echo 🚀 Starting Django Donation App Demo...
echo.

echo 📦 Step 1: Starting Docker container...
docker-compose -f docker-compose.local.yml up --build -d

echo ⏳ Waiting for app to start...
timeout /t 10 /nobreak

echo 🌐 Step 2: Your app is running locally at: http://localhost:8000
echo.

echo 🔗 Step 3: Creating public URL with ngrok...
echo.
echo 📋 INSTRUCTIONS FOR PUBLIC ACCESS:
echo 1. Download ngrok from: https://ngrok.com/download
echo 2. Sign up for free account at: https://ngrok.com
echo 3. Install ngrok and run: ngrok http 8000
echo 4. Share the public URL with your clients!
echo.

echo 🎯 Your Django app features:
echo ✅ Donation management system
echo ✅ School fees management  
echo ✅ Admin panel at /admin
echo ✅ User registration and login
echo ✅ Professional interface
echo.

echo 📊 Container status:
docker-compose -f docker-compose.local.yml ps

echo.
echo 🔧 To stop the demo: docker-compose -f docker-compose.local.yml down
echo 📋 To view logs: docker-compose -f docker-compose.local.yml logs -f web

pause
