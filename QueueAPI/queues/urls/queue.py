from django.urls import path
from queues.apiviews import queue_api


urlpatterns = [
    path("queues", queue_api.queue_list),
    path("queues/<int:pk>", queue_api.queue_detail),
]

# manual testing

# TestCase 1: check if a new queue is created
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=1 applicant_name=kenji no_applicant=3
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=2 applicant_name=shiela no_applicant=4
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=3 applicant_name=doy no_applicant=5
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=4 applicant_name=jeng no_applicant=6
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=5 applicant_name=catherine no_applicant=2
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=6 applicant_name=joevil no_applicant=1
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=7 applicant_name=katrina no_applicant=13
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=8 applicant_name=luis no_applicant=5
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=9 applicant_name=AJ no_applicant=2
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=10 applicant_name=pipay no_applicant=1
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=11 applicant_name=gabriel no_applicant=1
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=12 applicant_name=CK no_applicant=2
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=13 applicant_name=jewel no_applicant=1
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=14 applicant_name=zayden no_applicant=4
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=15 applicant_name=zack no_applicant=2
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=16 applicant_name=zander no_applicant=2
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=17 applicant_name=laurence no_applicant=1
# http POST http://127.0.0.1:8000/api/queues/v2/queues branch=1 service=18 applicant_name=mhae no_applicant=1 is_priority=true

# TestCase 2: check if distinct queue is fetched
# http http://127.0.0.1:8000/api/queues/v2/queues/1

# TestCase 3: check if distinct queue's service is updated
# http PATCH http://127.0.0.1:8000/api/queues/v2/queues/1 service=3

# TestCase 4: check if distinct queue's service and no of pax is updated
# http PATCH http://127.0.0.1:8000/api/queues/v2/queues/1 service=2 no_applicant=12

# TestCase 5: check if queue is called
# attributes that are needed
# called_by: string
# controller_id: sring
# is_called: boolean
# status: number
# http PATCH http://127.0.0.1:8000/api/queues/v2/queues/1 called_by="window 1" controller_id=123123124 is_called=true status=4

# TestCase 5: check if queue is done
# attributes that are needed
# status: number
# http PATCH http://127.0.0.1:8000/api/queues/v2/queues/1 status=1

# TestCase 5: check if queue is deleted
# http DELETE http://127.0.0.1:8000/api/queues/v2/queues/53

# TestCase 6: check if queues are be able to get
# http http://127.0.0.1:8000/api/queues/v2/queues

# TestCase 6: check if queues are be able to get filtered by branch id
# http GET http://127.0.0.1:8000/api/queues/v2/queues branch_id==2