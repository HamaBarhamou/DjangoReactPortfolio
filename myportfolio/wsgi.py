"""
WSGI config for myportfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.auth.models import User
from django.core.management import call_command
# from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')

application = get_wsgi_application()
# application=WhiteNoise(application)
app = application

# Vérifier si le superutilisateur existe déjà
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, 'admin@example.com', password)
