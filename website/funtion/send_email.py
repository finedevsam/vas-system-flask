from re import template
from flask import render_template_string, request, render_template
from .email_backend import EmailBackEnd
import threading

data = EmailBackEnd()

class EmailThread(threading.Thread):
    def __init__(self, html_content, email, email_subject):
        self.html_content = html_content
        self.email = email
        self.email_subject = email_subject
        threading.Thread.__init__(self)
    
    def run(self):
        data.sendEmail(self.html_content, self.email, self.email_subject)
        

class Email:


    def registration_email(self, email, fullname, tokens, **kwargs):
        url = request.url
        verify_link = f'http://{url}/verifyaccount?email={email}&token={tokens}'
        """ Sending Verification Email """
        html_content = render_template(
            'email/verify.html', data={'verify_link': verify_link, 'fullname': fullname}, **kwargs)
        """Call the Email Backend"""
        # data.sendEmail(html_content, email, emailSubject='Account Verification')
        EmailThread(html_content, email, email_subject='Account Verification').start()
        pass
    
    
    def merchant_reg(self, email, fullname, password, accesskey, **kwargs):
        """ Sending Verification Email """
        html_content = render_template_string(
            'email/merchant.html', data={'password': password, 'fullname': fullname, 'accesskey':accesskey}, **kwargs)
        """Call the Email Backend"""
        # data.sendEmail(html_content, email, emailSubject='Merchant Registration')
        EmailThread(html_content, email, email_subject='Merchant Registration').start()
        pass
    
    
    
    def resend_apikey(self, email, fullname, accesskey, **kwargs):
        """ Sending Verification Email """
        html_content = render_template_string(
            'email/apikey.html', data={'fullname': fullname, 'accesskey':accesskey}, **kwargs)
        """Call the Email Backend"""
        # data.sendEmail(html_content, email, emailSubject='API Key')
        EmailThread(html_content, email, email_subject='API Key').start()
        pass
    
    
    def send_code(self, email, fullname, code, **kwargs):
        """ Sending Verification Email """
        html_content = render_template_string(
            'email/code.html', data={'fullname': fullname, 'code':code}, **kwargs)
        """Call the Email Backend"""
        # send_email = data.sendEmail(html_content, email, emailSubject='OTP Code')
        EmailThread(html_content, email, email_subject='OTP Code').start()
        pass