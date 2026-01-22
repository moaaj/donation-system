# 🌐 ngrok Setup Guide - Internet Access for Your Django Project

This guide will help you expose your Django donation system to the internet using ngrok.

## 📥 Step 1: Download and Install ngrok

### Option A: Direct Download (Recommended)
1. Go to https://ngrok.com/download
2. Click "Download for Windows"
3. Extract the `ngrok.exe` file to a folder like `C:\ngrok\`
4. Add `C:\ngrok\` to your Windows PATH (optional but recommended)

### Option B: Using Package Manager
If you have Chocolatey installed:
```powershell
choco install ngrok
```

## 🔑 Step 2: Create ngrok Account and Get Auth Token

1. Go to https://ngrok.com/signup and create a free account
2. After signing up, go to https://dashboard.ngrok.com/get-started/your-authtoken
3. Copy your authtoken
4. Run this command (replace YOUR_TOKEN with your actual token):
```bash
ngrok config add-authtoken YOUR_TOKEN
```

## 🚀 Step 3: Start Your Django Application

### Method A: Using Docker (Recommended)
```bash
# Navigate to your project folder
cd "C:\Users\dell\Desktop\Final freelance project"

# Start the application
docker-compose up --build
```

### Method B: Using Python directly
```bash
# Navigate to your project folder
cd "C:\Users\dell\Desktop\Final freelance project"

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver 0.0.0.0:8000
```

## 🌐 Step 4: Expose to Internet with ngrok

Open a **NEW** terminal/command prompt and run:

```bash
ngrok http 8000
```

You'll see output like this:
```
ngrok                                                                                                                                                           
                                                                                                                                                                
Visit http://localhost:4040 for ngrok web interface                                                                                                            
                                                                                                                                                                
Session Status                online                                                                                                                            
Account                       Your Name (Plan: Free)                                                                                                           
Version                       3.x.x                                                                                                                             
Region                        United States (us)                                                                                                               
Latency                       45ms                                                                                                                              
Web Interface                 http://127.0.0.1:4040                                                                                                            
Forwarding                    https://abc123.ngrok-free.app -> http://localhost:8000                                                                          
                                                                                                                                                                
Connections                   ttl     opn     rt1     rt5     p50     p90                                                                                     
                              0       0       0.00    0.00    0.00    0.00
```

## 🎉 Step 5: Share with Clients

**Your public URL is**: `https://abc123.ngrok-free.app` (replace with your actual URL)

### What clients can access:
- **Main Application**: `https://your-url.ngrok-free.app`
- **Admin Panel**: `https://your-url.ngrok-free.app/admin`
- **All donation features**: Fully functional donation system

### Default Login (for admin):
- **Username**: admin
- **Password**: admin123

## 🔧 Important Settings for Internet Access

### Update Django Settings
Add your ngrok URL to allowed hosts. Create a `.env` file:

```env
# Copy from env.example and modify
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1,abc123.ngrok-free.app
DB_NAME=donation_db
DB_USER=donation_user
DB_PASSWORD=donation_password
DB_HOST=db
DB_PORT=5432
SITE_DOMAIN=https://abc123.ngrok-free.app
```

**Replace `abc123.ngrok-free.app` with your actual ngrok URL!**

## 🛡️ Security Considerations

### For Development/Testing:
- ✅ Perfect for client demos
- ✅ Great for testing with real users
- ✅ Easy to set up and share

### Important Notes:
- 🔄 **URL changes**: Free ngrok URLs change each time you restart
- 🔒 **Security**: Anyone with the URL can access your app
- ⏱️ **Session limits**: Free plan has 2-hour session limits
- 🌐 **Performance**: Slight latency due to tunneling

## 💡 Pro Tips

### 1. Keep ngrok Running
Keep the ngrok terminal window open. If you close it, the tunnel stops.

### 2. Monitor Traffic
Visit `http://localhost:4040` to see:
- All incoming requests
- Response times
- Request details
- Replay requests

### 3. Custom Subdomain (Paid Plan)
```bash
ngrok http 8000 --subdomain=mydonationapp
# Creates: https://mydonationapp.ngrok.io
```

### 4. Multiple Tunnels
```bash
# Terminal 1: Main app
ngrok http 8000

# Terminal 2: Database admin (if needed)
ngrok http 5050
```

## 🚨 Troubleshooting

### "This site can't be reached"
1. Make sure your Django server is running on port 8000
2. Check that ngrok is running and showing "online" status
3. Verify the URL is correct

### "Invalid Host header"
Add your ngrok URL to `ALLOWED_HOSTS` in settings or `.env` file

### ngrok command not found
1. Make sure ngrok.exe is in your PATH
2. Or run it with full path: `C:\ngrok\ngrok.exe http 8000`

### Database connection issues with Docker
```bash
# Reset everything
docker-compose down -v
docker-compose up --build
```

## 📱 Quick Demo Script

Here's what to tell your clients:

> "Hi! I've set up your donation system. You can access it at:
> 
> **🌐 Website**: https://your-ngrok-url.ngrok-free.app
> 
> **Features you can test**:
> - Make donations
> - Switch between English/Malay
> - View donation history
> - Admin panel (login: admin/admin123)
> 
> The system is fully functional and ready for testing!"

## 🎯 Next Steps

Once testing is complete, consider:
1. **Cloud deployment** (DigitalOcean, Heroku, AWS)
2. **Custom domain** setup
3. **SSL certificate** for production
4. **Database backup** strategy

---

**🎉 You're all set!** Your Django donation system is now accessible from anywhere in the world via ngrok.
