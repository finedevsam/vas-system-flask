from flask import Blueprint, flash, request, redirect
from flask import render_template
from flask.helpers import url_for
from .models import *
from .funtion.validator import Validator
from .funtion.user_manager import UserManager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_required, login_user, logout_user, current_user

validator = Validator()
user = UserManager()
auth = Blueprint("auth", __name__)


@auth.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    else:
        if request.method == "POST":
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    flash("Welcome to VAS {}".format(user.full_name), category='success')
                    login_user(user, remember=True)
                    return redirect (url_for('views.home'))
                else:
                    flash("Invalid Password", category='error')
                    return redirect(url_for('auth.login'))
            else:
                flash("User not Found", category='error')
            return redirect(url_for('auth.login'))
        else:
            return render_template('login.html')


@auth.route('/logout')
def logout():
    logout_user()
    flash("Good bye and Have a nice day", category='success')
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if password1 != password2:
            flash("Password is not Match", category="error")
        
        ## Check the length of Fullname ##    
        elif len(fullname) < 2:
            flash("Fullname must be greater than 2 character", category="error")
        
        ## Call the Validation Password to Validate Password ##    
        elif validator.passwordValidator(password1) == False:
            flash("Weak password. Password must be with 8-15 character and must contain special character", category='error')    
        else:
            ## Call the register function ##
            user.register(fullname, email, password1)
        return redirect(url_for('auth.signup'))
            
    else:
        return render_template("signup.html")

