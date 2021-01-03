# Upravljanje konfiguracijom softvera

Project for course "Upravljanje konfiguracijom softvera".

Team members:
- Sara Fojkar
- Jelena Stojaković
- Petar Ćurčin
- Aleksandar Petaković

## How to Use

To use this project, follow these steps:

1. Create your working environment. (tip: use `pipenv`)
2. Install Django (`$ pipenv install django`)
3. Enter venv shell (`$ pipenv shell`)
4. Run migrations (`$ python manage.py migrate`)
5. Run server (`$ python manage.py runserver`)

### Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.8 runtime environment.

### Deployment to Heroku

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate
    $ heroku ps:restart

### Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
- [SemaphoreCI](https://docs.semaphoreci.com/examples/heroku-deployment/)
