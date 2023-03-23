FROM python:3.10-alpine3.17
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
RUN ["python3", "manage.py", "migrate"]
RUN ["python3", "manage.py", "seed_db"]
RUN ["python3", "manage.py", "resync_seq"]
RUN ["mkdir", "media"]
EXPOSE 8000
CMD ["python3 manage.py runserver"]