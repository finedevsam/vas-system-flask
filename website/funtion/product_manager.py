from website.models import *
from flask import flash
from website import db
from flask_login import current_user
import random
import string


"""
Class to Manage Products
"""

class ProductManager:
    
    
    ## Function to add new Product to the system ##
    def add_product(self, product_name, product_category, charges, live_endpoint, test_endpoint):
        T=6
        res = ''.join(random.choices(string.digits, k=T))
        code = str(res)
        if product_category == "":
            flash("Please select product category", category='error')
        else:
            product = Products(
                product_name=product_name, 
                product_code=code, 
                product_category=product_category, 
                product_live_endpoint=live_endpoint,
                product_test_endpoint=test_endpoint,
                charges=charges
                )
            db.session.add(product)
            db.session.commit()
            flash("Product Added Successfully", category='success')
        
        pass
    
    
    def display_all_product(self):
        all_product = Products.query.filter()
        return all_product
    
    
    def customer_add_product(self, code):
        product = Products.query.filter_by(product_code=code).one()
        
        ## Check if the product is already added to the customer
        if CustomerProducts.query.filter_by(products_id=product.id, user_id=current_user.id).first():
            flash("You already have the Product on your list", category='warning')
        else:
            add_customer_product = CustomerProducts(
                product_name=product.product_name, 
                product_code=product.product_code,
                user_id=current_user.id,
                products_id=product.id
                )
            db.session.add(add_customer_product)
            db.session.commit()
            flash("You have added {} as part of your products.".format(product.product_name), category='success')
        pass