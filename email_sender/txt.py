from email.message import EmailMessage
from data import password
import ssl
import smtplib

email_sender = 'David.Ibehej@gmail.com'
email_password = password

email_receiver = 'David.Ibehej@seznam.cz'

subject = 'Subject of email'
body = ''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(em['From'], email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())