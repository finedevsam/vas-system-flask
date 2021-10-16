from website.models import *
from flask import flash
from website import db
import base64
import os
dest_dir = os.path.join('uploads')


def convert_image64(image):
    with open("website/{}/{}".format(dest_dir, image), "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    return converted_string


class UserManager:
    
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