# Generated by Django 5.1.1 on 2024-10-15 06:46

from django.db import migrations
from queues.seed import create_default_data

class Migration(migrations.Migration):

    dependencies = [
        ("queues", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_default_data)]
