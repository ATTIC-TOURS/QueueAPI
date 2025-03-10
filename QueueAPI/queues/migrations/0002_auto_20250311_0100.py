from django.db import migrations
from queues.seeds import default_data

class Migration(migrations.Migration):

    dependencies = [
        ("queues", "0001_initial"),
    ]
    
    operations = [
        migrations.RunPython(data)
        for data in default_data
    ]
