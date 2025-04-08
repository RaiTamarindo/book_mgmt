import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_mgmt.settings')
django.setup()

from django.contrib.auth import get_user_model
from decouple import config

User = get_user_model()

username = config('DJANGO_SUPERUSER_USERNAME', default='admin')
email = config('DJANGO_SUPERUSER_EMAIL', default='admin@example.com')
password = config('DJANGO_SUPERUSER_PASSWORD', default='admin')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created.")
else:
    print(f"Superuser '{username}' already exists.")
