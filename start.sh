#!/bin/bash

if [ -z "$SSH_CLIENT" ] && [ -n "$HEROKU_EXEC_URL" ];
then
    source <(curl --fail --retry 3 -sSL "$HEROKU_EXEC_URL")
fi

if [[ "$DYNO" =~ ^release.* ]];
then
    set -e
    python3 manage.py migrate
else
    exec pipenv run gunicorn uks.wsgi  -b 0.0.0.0:${PORT} --reload --access-logfile -
fi
