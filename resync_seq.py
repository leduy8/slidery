import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

connection_psql = psycopg2.connect(
    user=os.environ.get("DATABASE_USER"),
    password=os.environ.get("DATABASE_PASSWORD"),
    port=os.environ.get("DATABASE_PORT"),
    database=os.environ.get("DATABASE_NAME"),
    host="localhost",
)

with connection_psql.cursor() as cursor_psql:
    cursor_psql.execute(
        """
        SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
    """
    )
    for row in cursor_psql.fetchall():
        tablename = row[0]
        ignored_tables = ["django_session"]
        if tablename not in ignored_tables:
            cursor_psql.execute(
                f"""
                SELECT setval('{tablename}_id_seq', (SELECT MAX(id) FROM {tablename})+1);
            """
            )
