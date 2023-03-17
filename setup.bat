if exist venv\ (
    .\venv\Scripts\activate
) else (
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements-windows.txt
)
python manage.py migrate
python manage.py seed_db
python manage.py resync_seq
mkdir media