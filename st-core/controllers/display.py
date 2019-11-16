from services.db_Display import DBDisplay
from services.mqtt_client import MqttClient
import settings
import json

class DisplayController:
    @staticmethod
    def verificate(request: dict):
        display = json.loads(request.body.read().decode("utf-8"))
        display_db = DBDisplay.FindTag('sqlite:///entidades/DB.db',display['tag_id'])
        display_json = json.loads(display_db)
        return display_json

    def add(request: dict):
        display = json.loads(request)
        DBDisplay.AddTag('sqlite:///entidades/DB.db',display)
    
    def update(request: dict, mqtt_client: MqttClient):
        display = json.loads(request.body.read().decode("utf-8"))
        display_db = DBDisplay.FindTag('sqlite:///entidades/DB.db',display['tag_id'])
        display_json = json.loads(display_db)
        if display['tag_id']==display_json['tag_id']:
            if display['store']!=display_json['store']:
                DBDisplay.UpdateTag('sqlite:///entidades/DB.db',display['tag_id'],'store',display['store'])
            if display['location']!=display_json['location']:
                DBDisplay.UpdateTag('sqlite:///entidades/DB.db',display['tag_id'],'location',display['location'])
            if display['product']!=display_json['product']:
                DBDisplay.UpdateTag('sqlite:///entidades/DB.db',display['tag_id'],'product',display['product'])
        else:
            DisplayController.add(display)
        product = {
            "name":display['product'],
            "price":display['price'],
            "quantity":display['quantity'],
            "expiration":display['expiration'],
            "product_id":display['product_id'],
            "discount" = display['discount'],
            "description" = display['description']
        }
        if ProductController.update(product):
            mqtt_client.publish(
                topic=display['location'],
                payload=dumps(json.dumps(product))
            )
    
    def delet(request: dict):
        display = json.loads(request.body.read().decode("utf-8"))
        DBDisplay.DeleteTag('sqlite:///entidades/DB.db',display['tag_id'])



