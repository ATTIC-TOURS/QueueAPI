# Generated by Django 5.1.3 on 2025-01-05 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queues', '0011_rename_status_id_queue_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicetype',
            old_name='category_id',
            new_name='category',
        ),
    ]
