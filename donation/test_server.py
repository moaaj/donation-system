#!/usr/bin/env python
"""
Simple test to check if Django can start properly
"""
import os
import sys
import django
from django.conf import settings
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'donation.settings')
    
    try:
        django.setup()
        print("✅ Django setup successful!")
        print(f"✅ Settings module: {settings.SETTINGS_MODULE}")
        print(f"✅ Debug mode: {settings.DEBUG}")
        print(f"✅ Allowed hosts: {settings.ALLOWED_HOSTS}")
        
        # Test if we can run the server
        print("\n🚀 Starting Django server...")
        execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8000'])
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
