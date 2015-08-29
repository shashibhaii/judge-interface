#! /bin/bash
source env/bin/activate
cd webserver
gunicorn website.wsgi:application --bind=127.0.0.1:8000 --log-file=-
# gunicorn website.wsgi:application --bind=unix:LOCATION/gunicorn_socket --log-file=-
