import os
import platform

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Setup project"

    def handle(self, *args, **options):
        if platform.system() == "Windows":
            os.system("setup.bat")
        else:
            os.system("sh setup.sh")
