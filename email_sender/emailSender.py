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

        #content data
        self.body = ""
        self.subject = "Empty Subject"
        
        #Reciever data
        self.__email_receiver = 'David.Ibehej@seznam.cz'
        
        #EmailMassage set up
        self.__em = EmailMessage()

        self.__context = ssl.create_default_context()


    @property
    def email_receiver(self):
        
        return self.__email_receiver


    @email_receiver.setter
    def email_receiver(self, value):
        
        print("Reciever changed!!!")

        self.__em['To'] = value
        self.__email_receiver = value


    def __em_setup(self):
        """Seting up EmailMessage Object \n as.. From, To, Subject ..."""

        self.__em['From'] = self.__email_sender
        self.__em['To'] = self.__email_receiver
        self.__em['Subject'] = self.subject
        self.__em.set_content(self.body)


    def send_message(self):
        """Sending messege"""

        self.__em_setup() #seting up EmailMessage object

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = self.__context) as smtp:
            smtp.login(self.__email_sender, self.__email_password)
            smtp.sendmail(self.__email_sender, self.__email_receiver, self.__em.as_string())