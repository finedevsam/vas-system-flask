from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager


db = SQLAlchemy()

db_user = 'root'
db_pass = 'victoria1992'
db_host = 'localhost'
db_name = 'vas'

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'uwnusnwswdenjdnjwnjdnjedhhebhdbedjwhejhdbh'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4".format(db_user, db_pass, db_host, db_name)
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
     
    from .models import User, Profile
    
    create_database(app)
    
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

def create_database(app):
    db.create_all(app=app)
    print("Database Created")