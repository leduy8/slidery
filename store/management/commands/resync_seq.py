from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "Resync table's id sequence to the latest record"

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
            """
            )
            for row in cursor.fetchall():
                tablename = row[0]
                ignored_tables = ["django_session", "store_cart"]
                if tablename not in ignored_tables:
                    cursor.execute(
                        f"""
                        SELECT setval('{tablename}_id_seq', (SELECT MAX(id) FROM {tablename})+1);
                    """
                    )

    print("Data has been resynced")
