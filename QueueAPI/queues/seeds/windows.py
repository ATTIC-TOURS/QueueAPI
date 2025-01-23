windows = [
    {"name": "1"},
    {"name": "2"},
    {"name": "3"},
    {"name": "4"},
    {"name": "5"},
    {"name": "6"},
    {"name": "7"},
    {"name": "Japan Visa"},
    {"name": "Korea Visa"},
    {"name": "Ticketing"},
    {"name": "Cashier"},
]

def create_default_windows(apps, schema_editor):
    Window = apps.get_model("queues", "Window")
    for window in windows:
        Window.objects.create(
            name=window["name"],
        )