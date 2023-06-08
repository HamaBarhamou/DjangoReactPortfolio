"""
WSGI config for myportfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')

application = get_wsgi_application()

app = application
 
 
""" import os

from django.core.wsgi import get_wsgi_application
from django.contrib.auth.models import User
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
import django
django.setup()
from django.core.management import call_command

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

# Vérifier si le superutilisateur existe déjà
if not User.objects.filter(username='admin').exists():
    # Chargement des paramètres Django
    application = get_wsgi_application()

    # Créer un superutilisateur avec les informations fournies
    User.objects.create_superuser('username', 'hamabarhamou@gmail.com', 'passw0rd')
    

    # Réaffecter l'application WSGI
    app = application
else:
    app = get_wsgi_application()
 """