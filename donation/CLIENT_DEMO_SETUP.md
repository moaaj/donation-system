# 🚀 INSTANT CLIENT DEMO - Public URL Setup

## 🎯 Get Your Django App Live in 5 Minutes!

### Option 1: Automated Setup (Recommended)

**Just run this:**
```bash
create_public_url.bat
```

This will:
1. ✅ Start your Django app with Docker
2. ✅ Create a public URL with ngrok
3. ✅ Give you a link to share with clients

### Option 2: Manual Setup

#### Step 1: Start Your App
```bash
start_demo.bat
```

#### Step 2: Install Ngrok (One-time setup)
1. Go to: https://ngrok.com/download
2. Download ngrok for Windows
3. Sign up for free account
4. Extract ngrok.exe to your project folder

#### Step 3: Create Public URL
```bash
ngrok http 8000
```

## 🌐 Your Public Demo URL

Ngrok will give you a URL like:
```
https://abc123.ngrok.io
```

**Share this URL with your clients!**

## 🎯 What Your Clients Will See

✅ **Full Django Donation System**
- Donation management interface
- School fees management
- User registration and login
- Admin panel at `/admin`
- Professional, responsive design

✅ **Live Features**
- Real-time donation processing
- Student fee tracking
- Payment management
- Analytics dashboard
- Multi-language support

## 📊 Demo Management

### Start Demo:
```bash
create_public_url.bat
```

### Stop Demo:
```bash
docker-compose -f docker-compose.local.yml down
```

### View Logs:
```bash
docker-compose -f docker-compose.local.yml logs -f web
```

## 🔧 Troubleshooting

**App not starting?**
- Make sure Docker Desktop is running
- Check: http://localhost:8000

**Ngrok not working?**
- Sign up at ngrok.com (free)
- Get your auth token
- Run: `ngrok config add-authtoken YOUR_TOKEN`

**Need help?**
- Your app runs locally at: http://localhost:8000
- Admin panel: http://localhost:8000/admin
- Check Docker logs if issues occur

## 💡 Pro Tips

- Keep the ngrok window open while clients are testing
- The URL changes each time you restart ngrok (free version)
- For permanent URLs, upgrade to ngrok paid plan
- Your app data is stored in Docker volumes

---

**Your Django donation system is ready for client demos!** 🎉
