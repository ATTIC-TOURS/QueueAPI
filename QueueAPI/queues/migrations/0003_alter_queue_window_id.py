# Generated by Django 5.1.1 on 2024-10-08 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("queues", "0002_alter_mobile_printer_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="queue",
            name="window_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="queues.window",
            ),
        ),
    ]
