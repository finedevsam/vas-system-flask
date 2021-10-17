from website.models import *
from flask import flash
from website import db
import base64
import os
import secrets
import string
from .send_email import Email
from werkzeug.security import check_password_hash, generate_password_hash

send_email = Email()
dest_dir = os.path.join('uploads')


def convert_image64(image):
    with open("website/{}/{}".format(dest_dir, image), "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    return converted_string


class UserManager:
    
    def register(self, fullname, email, password):
        N = 100
        tokens = ''.join(secrets.choice(
        string.ascii_lowercase + string.digits)for i in range(N))
        if "@" not in email:
            flash("Invalid Email format", category="error")
        
        elif User.query.filter_by(email=email).first():
            flash("Email Taken", category='error')
        else:
            send_email.registration_email(email, fullname, tokens)
            new_user = User(full_name=fullname, email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            
            flash("Registration Successfully", category="success")
        
        pass
    
    def create_profile(self, state, address, image, mobile, user_id):
        
        new_profile = Profile(address=address, state=state, mobile=mobile, image64=image, user_id=user_id)
        db.session.add(new_profile)
        db.session.commit()
        flash("Profile Updated Successfully", category='success')
        
        pass
    
    def update_profile(self, state, address, mobile, user_id):
        
        profile = Profile.query.filter_by(user_id=user_id).one()
        profile.address = address
        profile.state = state
        profile.mobile = mobile
        db.session.add(profile)
        db.session.commit()
        flash("Profile Updated Successfully", category='success')
        pass
    
    
    def get_login_user(self, user_id):
        user = User.query.get(user_id)
        return user