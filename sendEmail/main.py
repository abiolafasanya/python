from email.message import EmailMessage
import ssl
import smtplib
from app2 import password 


sender_email = 'hezekiahfasanya@gmail.com'
password = password
email_address = ['susanfasanya2@gmail.com', 'harbiola78@gmail.com', 'fastbeetservices@gmail.com', 'sussanfarsa009@gmail.om']

subject = 'Why IMUN Zoom Invitation'

body = """
This message contains the link to the imun zoom invitation meeting which takes place at 8pm today, and we look forward to seeing you there. Please
"""
for email in email_address:
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = email
    msg.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg)

    print('Email sent to', email)



# mail = EmailMessage()
# mail['Subject'] = subject
# mail['From'] = sender_email
# mail['To'] = receiver_email
# mail.set_content(body)

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
#     server.login(sender_email, password)
#     server.send_message(mail)
#     print('Mail sent successfully')