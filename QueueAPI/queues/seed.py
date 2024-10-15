branches = [
    {"name": "Main Office", "password": "1234"},
    {"name": "SM Mall of Asia", "password": "1234"},
    {"name": "SM Megamall", "password": "1234"},
    {"name": "SM North Edsa", "password": "1234"},
    {"name": "SM Fairview", "password": "1234"},
    {"name": "SM Southmall", "password": "1234"},
    {"name": "SM Clark", "password": "1234"},
    {"name": "SM Cebu", "password": "1234"},
    {"name": "SM Davao", "password": "1234"},
]

services = [
    {"name": "Japan Visa"},
    {"name": "Korea Visa"},
    {"name": "Ticket"},
    {"name": "Claim Passport"},
    {"name": "Others"}
]

windows = [
    {"name": "Window 1"},
    {"name": "Window 2"},
    {"name": "Window 3"},
    {"name": "Window 4"},
    {"name": "Window 5"},
    {"name": "Window 6"},
    {"name": "Window 7"},
    {"name": "Japan Visa"},
    {"name": "Korea Visa"},
    {"name": "Ticketing"},
    {"name": "Cashier"},
]

statuses = [
    {"name": "complete"},
    {"name": "pending"},
    {"name": "waiting"},
    {"name": "in-progress"},
    {"name": "cancel"},
]

mark_queues = [
    {"branch_id": 1, "text": "Welcome to Attic Tours!"},
    {"branch_id": 1, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 2, "text": "Welcome to Attic Tours!"},
    {"branch_id": 2, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 3, "text": "Welcome to Attic Tours!"},
    {"branch_id": 3, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 4, "text": "Welcome to Attic Tours!"},
    {"branch_id": 4, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 5, "text": "Welcome to Attic Tours!"},
    {"branch_id": 5, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 6, "text": "Welcome to Attic Tours!"},
    {"branch_id": 6, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 7, "text": "Welcome to Attic Tours!"},
    {"branch_id": 7, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 8, "text": "Welcome to Attic Tours!"},
    {"branch_id": 8, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 9, "text": "Welcome to Attic Tours!"},
    {"branch_id": 9, "text": "Please issue a queue and wait for to be called!"},
]


def create_default_data(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Branch = apps.get_model("queues", "Branch")
    for branch in branches:
        Branch.objects.create(
            name=branch["name"],
            password=branch["password"]
        )
    
    Service = apps.get_model("queues", "Service")
    for service in services:
        Service.objects.create(
            name=service["name"],
        )
    
    Window = apps.get_model("queues", "Window")
    for window in windows:
        Window.objects.create(
            name=window["name"],
        )
    
    Status = apps.get_model("queues", "Status")
    for status in statuses:
        Status.objects.create(
            name=status["name"],
        )
    
    MarkQueue = apps.get_model("queues", "MarkQueue")
    for mark_queue in mark_queues:
        MarkQueue.objects.create(
            branch_id=Branch.objects.get(id=mark_queue["branch_id"]),
            text=mark_queue["text"]
        )