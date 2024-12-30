from django.core.mail import send_mail
from django.conf import settings
import pytz


def greetings(name, queue_code, datetime, category_name, service_name):
    manila_tz = pytz.timezone(settings.TIME_ZONE)
    return f"""<html>
                <head>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            font-size: 26px;
                            background-color: #f4f4f4;
                            margin: 0;
                            padding: 20px;
                        }}
                        .container {{
                            width: 360px;
                            margin: 0 auto;
                            background-color: #fff;
                        
                            border-radius: 5px;
                            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        }}
                        div img {{
                            width: 100%;
                            height: 75px;
                        }}
                        .content {{
                            width: 320px;
                            margin: 0 auto;
                            padding: 20px;
                            margin-top: 20px;
                            color: black;
                        }}
                        .content p {{
                            color: black;
                        }}
                        .footer {{
                            width: 320px;
                            margin: 0 auto;
                            padding: 20px;
                            font-size: 12px;
                            color: #777;
                        }}
                        .footer img {{
                            height: 20px;
                            width: 30px;
                        }}

                        article {{
                            margin-top: 80px;
                            margin-bottom: 80px;
                            text-align: left;
                            color: black;
                        }}

                        article h1 {{
                            font-size: 32px;
                            font-weight: lighter;
                            text-align: center;
                            margin-bottom: 8px;
                            color: black;
                        }}

                        article p {{
                            font-size: 32px;
                            font-weight: 900;
                            text-align: center;
                            margin: 0px;
                            color: black;
                        }}

                        article h2 {{
                            margin-top: 50px;
                            font-size: 18px;
                            color: black;
                        }}
                        article ul {{
                            color: black;
                        }}
                        
                        article ul li {{
                            color: black;
                        }}

                        .bold {{
                            font-weight: 900;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div>
                            <img src="https://raw.githubusercontent.com/ATTIC-TOURS/static/main/banner.png" />
                        </div>
                        <div class="content">
                            <p>Dear <span class="bold">{name}</span>,</p>
                            <p>Thank you for applying at Attic Tours.</p>
                            <p>Your request has been successfully received.</p>

                            <article>
                                <h1>Your Queue Number</h1>
                                <p>{queue_code}</p>

                                <h2>Details of your Request:</h2>
                                <ul>
                                    <li><span class="bold">Date of Request</span>: {datetime.astimezone(manila_tz).strftime('%B %d, %Y %I:%M %p ')}</li>
                                    <li><span class="bold">Service</span>: {category_name} / {service_name}</li>
                                </ul>
                            </article>

                            <p>“As your queue number approaches, 
                                you will receive a notification email to keep you updated on your status.”</p>

                        </div>
                        <div class="footer">
                            <p>Thank you for using our service! </p>
                            <p><img src="https://raw.githubusercontent.com/ATTIC-TOURS/static/main/attic_logo.png" />
                            </p>
                        </div>
                    </div>
                </body>
                </html>
            """

def send_greetings(email_address, queue_info):
    name = queue_info["name"]
    queue_code = queue_info["queue_code"]
    datetime = queue_info["datetime"]
    category_name = queue_info["category_name"]
    service_name = queue_info["service_name"]
    try:
        subject = "[QUEUE] Thank you for applying Attic tours"
        message = f"Hi {name},\n\nThank you for applying at Attic Tours.\nYour queue number is {queue_code}.\nWait for the notification.\nThank you."
       
        send_mail(
            subject, 
            message, 
            settings.EMAIL_HOST_USER, 
            [email_address],
            html_message=greetings(
                name, queue_code, datetime, category_name, service_name
            ))
        
    except Exception as e:
        print(f"sending email error: {e}")