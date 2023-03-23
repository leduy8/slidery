#! /bin/bash

pip3 install wheel
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py seed_db
python3 manage.py resync_seq
mkdir media
python3 manage.py runserver 0.0.0.0:8000 --noreload