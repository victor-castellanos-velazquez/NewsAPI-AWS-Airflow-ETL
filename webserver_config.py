"""Default configuration for the Airflow webserver."""

from __future__ import annotations

import os

from flask_appbuilder.const import AUTH_DB

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
WTF_CSRF_TIME_LIMIT = None

AUTH_TYPE = AUTH_DB

# Configuración de Gunicorn
GUNICORN_CMD_ARGS = "--timeout 300 --workers 4 --worker-class gthread --threads 4"

# Aumentar el timeout del webserver
WEBSERVER_WORKER_TIMEOUT = 300