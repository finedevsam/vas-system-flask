import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import pathlib
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

"""Declare function to get Email configuration"""



class EmailBackEnd:
    
    def sendEmail(self, template, receiverEmail, emailSubject):
        print(receiverEmail)
        email_sender = environ.get('SENDER_EMAIL')
        print(email_sender)
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = receiverEmail
        msg['Subject'] = emailSubject

        msg.attach(MIMEText(template, 'html'))

    
        # msg.attach(part)

        try:
            server = smtplib.SMTP(environ.get('SMTP_HOST'), environ.get('EMAIL_PORT'))
            server.ehlo()
            server.starttls()
            server.login(environ.get('SENDER_USER'), environ.get('EMAIL_PASS'))
            text = msg.as_string()
            server.sendmail(email_sender, receiverEmail, text)
            print('email sent')
            server.quit()
        except:
            print("SMPT server connection error")
        return True


    def sendEmailWithFile(self, template, emailSubject, receiverEmail, pathToFile, docName):
        
        # data = emailConfig()
        sender_email = environ.get('SENDER_EMAIL')
        username = environ.get('SENDER_USER')
        password = environ.get('SENDER_PASS')
        port = environ.get('SENDER_PORT')
        host = environ.get('SMTP_HOST')

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = environ.get('SENDER_EMAIL')
        message["To"] = receiverEmail
        message["Subject"] = emailSubject

        message.attach(MIMEText(template, "html"))

        # filename = './cv.pdf'  # In same directory as script

        # Open PDF file in binary mode
        with open(pathToFile, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)
        file_extension = pathlib.Path(pathToFile).suffix
        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {docName}{file_extension}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        # context = ssl.create_default_context()
        if environ.get('SSL', default=False, cast=bool) == False:
            with smtplib.SMTP(host, port) as server:
                server.login(username, password)
                server.sendmail(sender_email, receiverEmail, text)
        else:
            with smtplib.SMTP_SSL(host, port) as server:
                server.login(username, password)
                server.sendmail(sender_email, receiverEmail, text)
        pass