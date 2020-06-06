import smtplib
import config

def send_email(subject, message, recipient_email):
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = "Subject: {}\n\n{}".format(subject, message)
        server.sendmail(config.EMAIL_ADDRESS, recipient_email, message)
        server.quit()
        print("Email sent.")
    except:
        print("Email failed.")


subject = "TEST: This is a test email subject line"
message = \
"""
<This is a script sending you all an email. :D> 

<Announcement content.>

<Signature content>
"""
bcc_to = ["", "", ""] #Add a list of recipients. 

for i in bcc_to:
    send_email(subject, message, i)