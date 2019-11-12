from services.mqtt_client import MqttClient
from controllers.display import DisplayController
from services.db_Product import DBProduct
import json


class ProductController:

    @staticmethod
    def update(location: dict, request: dict, mqtt_client: MqttClient):
        product = json.loads(request)
        display = json.loads(location)
        localitation = display['location']
        display_local = json.loads(localitation)
        mqtt_client.publish(
            topic=display_local,
            payload=dumps(product)
        )
        DisplayController.update(display)
        product_db = DBProduct.FindProduct('sqlite:///entidades/DB.db',product['name'])
        product_json = json.loads(product_db)
        if product['name']==product_json['name']:
            if product['price']!=product_json['price']:
                DBProduct.UpdateProduct('sqlite:///entidades/DB.db',display['name'],'price',display['price'])
            if product['quantity']!=product_json['quantity']:
                DBProduct.UpdateProduct('sqlite:///entidades/DB.db',display['name'],'quantity',display['quantity'])
            if product['expiration']!=product_json['expiration']:
                DBProduct.UpdateProduct('sqlite:///entidades/DB.db',display['name'],'expiration',display['expiration'])
            if product['product_id']!=product_json['product_id']:
                DBProduct.UpdateProduct('sqlite:///entidades/DB.db',display['name'],'product_id',display['product_id'])
            if product['discount']!=product_json['discount']:
                DBProduct.UpdateProduct('sqlite:///entidades/DB.db',display['name'],'discount',display['discount'])
            if product['description']!=product_json['description']:
                DBProduct.UpdateProduct('sqlite:///entidades/DB.db',display['name'],'description',display['description'])
        else:
            ProductController.add(product)
        return product

    def add(request: dict):
        product = json.loads(request)
        DBProduct.AddTag('sqlite:///entidades/DB.db',product)
    
    def delete(request: dict):
        product = json.loads(request)
        DBProduct.DeleteProduct('sqlite:///entidades/DB.db',product['name'])