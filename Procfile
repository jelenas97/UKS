web: pipenv run gunicorn uks.wsgi:application --log-file - --log-level debug
     pipenv run python manage.py collectstatic --noinput
     pipenv run python manage.py migrate