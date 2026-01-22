@echo off
cd /d "C:\Users\dell\Desktop\Final freelance project\donation"
call venv\Scripts\activate.bat
python manage.py runserver 0.0.0.0:8000
pause
