branches = [
    {"name": "Main Office", "password": "mainoffice"},
    {"name": "SM Mall of Asia", "password": "2022"},
    {"name": "SM North Edsa", "password": "1234"},
    {"name": "SM Megamall", "password": "1234"},
    {"name": "SM Fairview", "password": "arviepogi"},
    {"name": "SM Southmall", "password": "1234"},
    {"name": "SM Clark", "password": "1234"},
    {"name": "SM Cebu", "password": "1234"},
    {"name": "SM Davao", "password": "1234"},
]


def create_default_branches(apps, schema_editor):
    Branch = apps.get_model("queues", "Branch")
    for branch in branches:
        Branch.objects.create(
            name=branch["name"],
            password=branch["password"]
        )