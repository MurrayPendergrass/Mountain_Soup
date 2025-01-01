import os
import smtplib
from email.message import EmailMessage


def send_email(to, area_list):

    routes = ", ".join(str(x) for x in area_list)
    message = "Hello, the following areas have new routes on Mountain Project: " + routes
    
    try:
        email_address = "MountainSoup.Project@gmail.com"
        email_password = "aiai vzuh xfrg atpv"

        # create email
        msg = EmailMessage()
        msg['Subject'] = "New Routes"
        msg['From'] = "MountainSOup.Project@gmail.com"
        msg['To'] = to
        msg.set_content(message)

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
        return True

    except Exception as e:
        print("Problem during send email")
        print(str(e))
    return False









#import smtplib

#def send_message(email, area_list):

#routes = ", ".join(str(x) for x in area_list)
#message = "Hello, the following areas have new routes on Mountain Project: "

#server = smtplib.SMTP('smtp.gmail.com', 587)
#server.starttls()
#server.login("murraypendergrass4@gmail.com", "ived suuu rhrp uslr")

#msg = "Hello! This Message was sent by the help of Python"

#Send the mail
#server.sendmail("murraypendergrass4@gmail.com", "murraypendergrass0@gmail.com", msg)