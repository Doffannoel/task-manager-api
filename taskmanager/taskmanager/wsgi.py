import os
import sys

# Manually set absolute paths
sys.path.append('/app/task-manager-api/taskmanager')
sys.path.append('/app/task-manager-api')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()