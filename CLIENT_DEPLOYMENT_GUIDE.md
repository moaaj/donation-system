# 🚀 Django Donation System - Client Deployment Guide

This guide will help you quickly set up and run the Django Donation System using Docker.

## 📋 Prerequisites

Before you begin, make sure you have the following installed on your system:

- **Docker Desktop** (Windows/Mac) or **Docker Engine** (Linux)
- **Docker Compose** (usually included with Docker Desktop)

### Installing Docker

#### Windows:
1. Download Docker Desktop from: https://www.docker.com/products/docker-desktop/
2. Run the installer and follow the setup wizard
3. Restart your computer when prompted
4. Open Docker Desktop and wait for it to start

#### Mac:
1. Download Docker Desktop from: https://www.docker.com/products/docker-desktop/
2. Drag Docker to Applications folder
3. Launch Docker from Applications
4. Follow the setup instructions

#### Linux (Ubuntu/Debian):
```bash
# Update package index
sudo apt update

# Install Docker
sudo apt install docker.io docker-compose

# Add your user to docker group
sudo usermod -aG docker $USER

# Restart your session or reboot
```

## 🏃‍♂️ Quick Start (3 Simple Steps)

### Step 1: Download the Project
Extract the project files to a folder on your computer.

### Step 2: Open Terminal/Command Prompt
Navigate to the project folder:
```bash
cd path/to/your/project/folder
```

### Step 3: Run the Application
```bash
docker-compose up --build
```

That's it! The application will be available at:
- **Main Application**: http://localhost:8000
- **Database Admin** (pgAdmin): http://localhost:5050

## 🔐 Default Login Credentials

### Django Admin (http://localhost:8000/admin/)
- **Username**: admin
- **Password**: admin123

### Database Admin - pgAdmin (http://localhost:5050)
- **Email**: admin@example.com
- **Password**: admin123

## 📱 Application Features

Your Django Donation System includes:

1. **Multi-language Support** (English/Malay)
2. **Donation Management**
3. **School Fees Management**
4. **Waqaf (Islamic Endowment) System**
5. **QR Code Generation**
6. **Admin Dashboard**

## 🛠️ Advanced Configuration

### Environment Variables
Copy `env.example` to `.env` and modify as needed:
```bash
cp env.example .env
```

Edit `.env` file to customize:
- Database credentials
- Django secret key
- Debug settings
- Email configuration

### Database Management
Access pgAdmin at http://localhost:5050 to:
- View database tables
- Run SQL queries
- Backup/restore data
- Monitor database performance

### Stopping the Application
```bash
# Stop the application
docker-compose down

# Stop and remove all data (fresh start)
docker-compose down -v
```

### Viewing Logs
```bash
# View all logs
docker-compose logs

# View specific service logs
docker-compose logs web
docker-compose logs db
```

## 🌐 Making it Accessible to Others

### Option 1: Local Network Access
1. Find your computer's IP address:
   - Windows: `ipconfig`
   - Mac/Linux: `ifconfig` or `ip addr`

2. Update the `ALLOWED_HOSTS` in `.env`:
   ```
   ALLOWED_HOSTS=localhost,127.0.0.1,YOUR_IP_ADDRESS
   ```

3. Restart the application:
   ```bash
   docker-compose down
   docker-compose up
   ```

4. Others can access via: `http://YOUR_IP_ADDRESS:8000`

### Option 2: Using ngrok (Internet Access)
1. Install ngrok: https://ngrok.com/download
2. Run ngrok:
   ```bash
   ngrok http 8000
   ```
3. Share the ngrok URL with your clients

### Option 3: Cloud Deployment
For production deployment, consider:
- **DigitalOcean App Platform**
- **Heroku**
- **AWS ECS**
- **Google Cloud Run**

## 🔧 Troubleshooting

### Common Issues:

#### Port Already in Use
```bash
# Check what's using port 8000
netstat -ano | findstr :8000  # Windows
lsof -i :8000                 # Mac/Linux

# Use different ports
docker-compose -f docker-compose.yml up --build
```

#### Docker Permission Issues (Linux)
```bash
sudo usermod -aG docker $USER
# Logout and login again
```

#### Database Connection Issues
```bash
# Reset database
docker-compose down -v
docker-compose up --build
```

#### Application Not Loading
1. Check if Docker is running
2. Verify ports are not blocked by firewall
3. Check logs: `docker-compose logs web`

## 📞 Support

If you encounter any issues:

1. **Check the logs**: `docker-compose logs`
2. **Restart the application**: `docker-compose restart`
3. **Fresh start**: `docker-compose down -v && docker-compose up --build`

## 🎯 Production Checklist

Before deploying to production:

- [ ] Change default passwords
- [ ] Set `DEBUG=False` in `.env`
- [ ] Configure proper email settings
- [ ] Set up SSL/HTTPS
- [ ] Configure backup strategy
- [ ] Set up monitoring
- [ ] Update `ALLOWED_HOSTS` for your domain

---

## 📝 Quick Commands Reference

```bash
# Start application
docker-compose up --build

# Stop application
docker-compose down

# View logs
docker-compose logs

# Access Django shell
docker-compose exec web python manage.py shell

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Run migrations
docker-compose exec web python manage.py migrate

# Collect static files
docker-compose exec web python manage.py collectstatic
```

---

**🎉 Congratulations!** Your Django Donation System is now ready to use. The application provides a complete donation management platform with multi-language support and modern web interface.
