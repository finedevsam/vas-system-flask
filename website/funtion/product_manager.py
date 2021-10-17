from website.models import *
from flask import flash
from website import db
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