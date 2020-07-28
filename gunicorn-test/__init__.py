#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# gunicorn --workers 8 --bind 0.0.0.0:8001 flask_app:app
from gunicorn.app.pasterapp import serve