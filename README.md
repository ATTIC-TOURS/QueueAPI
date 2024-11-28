# QueueAPI

**to run**

_localhost_
option 1: python3 manage.py runserver

_selected ip address__
option 2: python3 manage.py runserver IP_ADDRESS:PORT_NUMBER

_uvicorn locahost_ (path where the manage.py is)
option 3: uvicorn QueueAPI.asgi:application 

_uvicorn selected ip address_
option 4: uvicorn QueueAPI.asgi:application --host IP_ADDRESS --port PORT_NUMBER