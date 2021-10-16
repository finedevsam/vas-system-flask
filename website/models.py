from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_registered = db.Column(db.DateTime(timezone=True), default=func.now())
    profile = db.relationship('Profile', back_populates="user", uselist=False)
    


class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(150))
    state = db.Column(db.String(150))
    mobile = db.Column(db.String(150))
    image64 = db.Column(db.UnicodeText)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship("User", back_populates="profile")
    


class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(150))
    product_code = db.Column(db.String(150))
    product_category = db.Column(db.String(150))
    product_live_endpoint = db.Column(db.String(150))
    product_test_endpoint = db.Column(db.String(150))
    charges = db.Column(db.String(150))
    is_active = db.Column(db.Boolean, default=True)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())



class CustomerProducts(db.Model):
    __tablename__ = 'customer_products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(150))
    product_code = db.Column(db.String(150))
    product_key = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    products_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    
    
    