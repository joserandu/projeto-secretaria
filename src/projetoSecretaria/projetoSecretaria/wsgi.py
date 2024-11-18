"""
WSGI config for projetoSecretaria project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# Add the project directory to the sys.path
project_home = '/home/Randu/projeto-secretaria/src/projetoSecretaria'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'projetoSecretaria.settings'

# Activate the virtualenv
activate_this = '/home/Randu/projeto-secretaria/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import Django WSGI handler to serve the application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
