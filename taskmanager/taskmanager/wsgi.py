"""
WSGI config for taskmanager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Calculate the path to the project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Add the project directory to the Python path
sys.path.append(str(BASE_DIR))

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

# Get the WSGI application
application = get_wsgi_application()