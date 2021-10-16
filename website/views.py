from flask import Flask, Blueprint, render_template, redirect, flash, request
from sqlalchemy.sql.functions import user
from .funtion.user_manager import UserManager
from flask.helpers import url_for
from werkzeug.utils import secure_filename
from .models import *
import os
from flask_login import login_required, current_user

dest_dir = os.path.join('uploads')

views = Blueprint("views", __name__)
users = UserManager()

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@views.route('/home')
@login_required
def home():
    current_page = 'current-page'
    return render_template('home.html', home_current_page=current_page)


@views.route('/profile/', methods=['GET', 'POST'])
@login_required
def profile():
    current_page = 'current-page'
    if request.method == "POST":
        address = request.form.get('address')
        state = request.form.get('state')
        mobile = request.form.get('mobile')
        file = request.files['file']
        if Profile.query.filter_by(user_id=current_user.id).first():
            users.update_profile(state, address, mobile, user_id=current_user.id)
        else:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(f'website/static/{dest_dir}', filename))
                users.create_profile(state, address, filename, mobile, user_id=current_user.id)
            else:
                flash("Invalid File Format", category='error')
        return redirect(url_for('views.profile'))
    else:
        return render_template('profile.html', user=current_user, profile_current_page=current_page)


    
@views.route('/products/', methods=['GET', 'POST'])
def products():
    current_page = 'current-page'
    return render_template('products.html', product_current_page=current_page)