import os
from django.core.wsgi import get_wsgi_application

# ✅ Ensures Django correctly loads settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

application = get_wsgi_application()

