[ -d "$(pwd)/venv" ] && source venv/bin/activate || python3 -m venv venv ; source venv/bin/activate ; pip install -r requirements.txt
python manage.py migrate
python manage.py seed_db
python manage.py resync_seq
mkdir media