# Generated by Django 5.1.3 on 2025-01-05 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queues', '0014_rename_branch_id_mobile_branch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='printer',
            old_name='branch_id',
            new_name='branch',
        ),
    ]
