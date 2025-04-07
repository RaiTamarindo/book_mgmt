import os
import django
from django.core.management import execute_from_command_line

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adapters.django.settings")
    django.setup()

    port = os.getenv("API_PORT", "8000")

    execute_from_command_line(["manage.py", "runserver", f"0.0.0.0:{port}"])

if __name__ == "__main__":
    main()
