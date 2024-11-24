# Installing the command-line tools

pip install --upgrade pythonanywhere

# Creating a website

pa website create --domain attictoursdeveloper.pythonanywhere.com --command '/home/attictoursdeveloper/.venv/bin/uvicorn --app-dir /home/attictoursdeveloper/QueueAPI/QueueAPI --uds ${DOMAIN_SOCKET} QueueAPI.asgi:application'

## COMMAND to use

/home/attictoursdeveloper/.venv/bin/uvicorn --app-dir /home/attictoursdeveloper/QueueAPI/QueueAPI --uds ${DOMAIN_SOCKET} QueueAPI.asgi:application

# Reloading (when you change the code)

pa website reload --domain attictoursdeveloper.pythonanywhere.com


**Reference**

(Deploying ASGI sites on PythonAnywhere (beta))[https://help.pythonanywhere.com/pages/ASGICommandLine/#django]