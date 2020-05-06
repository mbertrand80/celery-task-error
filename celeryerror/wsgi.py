"""
WSGI config for celeryerror project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
import newrelic.agent

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celeryerror.settings")

def NewRelicWrapper(application):
    path = settings.BASE_DIR + '/newrelic.ini'
    newrelic.agent.initialize(path, environment='development')

    return newrelic.agent.wsgi_application()(application)


application = get_wsgi_application()
application = NewRelicWrapper(application)
