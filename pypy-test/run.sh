#!/bin/sh
gunicorn --name 'Gunicorn App Gevent'  --bind 0.0.0.0:8004 server:app --workers 8
