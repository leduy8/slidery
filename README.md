# django-learning

## Installation

Python 3.8+
PostgreSQL 8+
Create database for the project
Setup .env file

### Install the virtual environment and its packages and start the server.

```sh
cd django-learning
python3 -m venv venv
source venv/bin/activate
```

### Setup data

```sh
python manage.py migrate
python manage.py seed_db
python manage.py resync_seq
python manage.py createsuperuser # To create admin user
```

### Start the server

```sh
python manage.py runserver
```
