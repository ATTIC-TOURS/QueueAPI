branches = [
    {"name": "Main Office", "password": "mainoffice"},
    {"name": "SM Mall of Asia", "password": "2022"},
    {"name": "SM North Edsa", "password": "8888"},
    {"name": "SM Megamall", "password": "kamegamega"},
    {"name": "SM Fairview", "password": "arviepogi"},
    {"name": "SM Southmall", "password": "2024"},
    {"name": "SM Clark", "password": "clark"},
    {"name": "SM Cebu", "password": "cebu"},
    {"name": "SM Davao", "password": "davao"},
]


def create_default_branches(apps, schema_editor):
    Branch = apps.get_model("queues", "Branch")
    for branch in branches:
        Branch.objects.create(
            name=branch["name"],
            password=branch["password"]
        )