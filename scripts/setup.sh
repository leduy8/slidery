#! /bin/bash

firstRun() {
    python3 -m venv venv
    source $(pwd)/venv/bin/activate
    pip install wheel
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py seed_db
    python manage.py resync_seq
    mkdir media
}

[ -d "$(pwd)/venv" ] && source $(pwd)/venv/bin/activate || firstRun
