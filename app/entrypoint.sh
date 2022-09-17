#!/bin/bash
nginx
gunicorn -w ${WORKERS:-4} --bind unix:imgpush.sock wsgi:app --access-logfile -
