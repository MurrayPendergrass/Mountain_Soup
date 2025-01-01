import mtnsoup_loadvalues
import mtnsoup_comparison
import mtnsoup_overwrite
#import mtnsoup_sendtxt
import mtnsoup_sendemail
import os
import smtplib
from email.message import EmailMessage

#counts are wrong for some climbing areas#


#####################################################################
#Load Values
df = mtnsoup_loadvalues.get_values()


#####################################################################
#Make Comparison
newroutes = mtnsoup_comparison.make_comparison(df)


#####################################################################
#Overwrite
mtnsoup_overwrite.overwrite()


#####################################################################
#Send Text
text_list = ['murraypendergrass0@gmail.com']

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

if len(newroutes) > 0:
    for a in text_list:
        mtnsoup_sendemail.send_email(a, newroutes)

    