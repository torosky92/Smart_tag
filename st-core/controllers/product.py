from services.db_Product import DBProduct
import json


class ProductController:

    @staticmethod
    def update(request: dict):
        product = json.loads(request.body.read().decode("utf-8"))
        product_db = DBProduct.FindProduct('sqlite:///entidades/DB.db',product['name'])
        product_json = json.loads(product_db)
        if product['name']==product_json['name']:
            if product['price']!=product_json['price']:
                DBProduct.UpdateProduct('sqlite:///entidades/DB.db',product['name'],'price',product['price'])
            if product['quantity']!=product_json['quantity']:
                DBProduct.UpdateProduct('sqlite:///entidades/DB.db',product['name'],'quantity',product['quantity'])
            if product['expiration']!=product_json['expiration']:
                DBProduct.UpdateProduct('sqlite:///entidades/DB.db',product['name'],'expiration',product['expiration'])
            if product['product_id']!=product_json['product_id']:
                DBProduct.UpdateProduct('sqlite:///entidades/DB.db',product['name'],'product_id',product['product_id'])
            if product['discount']!=product_json['discount']:
                DBProduct.UpdateProduct('sqlite:///entidades/DB.db',product['name'],'discount',product['discount'])
            if product['description']!=product_json['description']:
                DBProduct.UpdateProduct('sqlite:///entidades/DB.db',product['name'],'description',product['description'])
        else:
            ProductController.add(request)
        return True

    @staticmethod
    def updateQuantity(request: dict):
        product = json.loads(request.body.read().decode("utf-8"))
        product_db = DBProduct.FindProduct('sqlite:///entidades/DB.db',product['name'])
        product_json = json.loads(product_db)
        if product['name']==product_json['name']:
            if product['quantity']!=product_json['quantity']:
                DBProduct.UpdateProduct('sqlite:///entidades/DB.db',product['name'],'quantity',product['quantity'])
                return True
        return False

    def add(request: dict):
        DBProduct.AddProduct('sqlite:///entidades/DB.db',request)
    
    def delete(request: dict):
        product = json.loads(request.body.read().decode("utf-8"))
        DBProduct.DeleteProduct('sqlite:///entidades/DB.db',product['name'])