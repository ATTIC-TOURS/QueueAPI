from django.urls import path
from queues.apiviews import branch_api


urlpatterns = [
    path("branches", branch_api.branch_list),
    path("branch_login", branch_api.branch_login),
]

# manual testing

# TestCase 1: check if branches are all set
# http http://127.0.0.1:8000/api/queues/v2/branches

# TestCase 2: check if login is ok with correct password
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=1 password=mainoffice
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=2 password=2022
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=3 password=8888
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=4 password=kamegamega
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=5 password=arviepogi
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=6 password=2024
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=7 password=clark
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=8 password=cebu
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=9 password=davao

# TestCase 3: check if login is ok with incorrect password
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=1 password=mainoffice1
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=2 password=20221
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=3 password=88881
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=4 password=kamegamega1
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=5 password=arviepogi1
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=6 password=20241
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=7 password=clark1
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=8 password=cebu1
# http http://127.0.0.1:8000/api/queues/v2/branch_login branch_id=9 password=davao1