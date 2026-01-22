@echo off
echo Starting Django server for ngrok...
cd /d "C:\Users\dell\Desktop\Final freelance project\donation"
call venv\Scripts\activate.bat
echo Virtual environment activated
python manage.py runserver 0.0.0.0:8000
pause
