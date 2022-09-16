from email.message import EmailMessage
from data import password
import ssl
import smtplib

class EmailSender():

    '''Email sending class'''

    def __init__(self):
        
        #Sender data
        self.__email_sender = 'David.Ibehej@gmail.com'
        self.__email_password = password
        
        #Reciever data
        self.__email_receiver = 'David.Ibehej@seznam.cz'
        
        #EmailMassage set up
        self.__em = EmailMessage()

        self.__em['From'] = self.__email_sender
        self.__em['To'] = self.__email_receiver


    @property
    def email_receiver(self):
        
        return self.__email_receiver


    @email_receiver.setter
    def email_receiver(self, value):
        
        print("Value setted")

        self.__em['To'] = value
        self.__email_receiver = value


    def send_message(self, subject, body):
        
        self.__em['Subject'] = subject
        self.__em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
            smtp.login(self.__email_sender, self.__email_password)
            smtp.sendmail(self.__email_sender, self.__email_receiver, self.__em.as_string())