statuses = [
    {"name": "complete"},
    {"name": "pending"},
    {"name": "waiting"},
    {"name": "now-serving"},
    {"name": "return"},
]

def create_default_statuses(apps, schema_editor):
    Status = apps.get_model("queues", "Status")
    for status in statuses:
        Status.objects.create(
            name=status["name"],
        )