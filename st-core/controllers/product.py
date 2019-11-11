from models.product import Product
from services.mqtt_client import MqttClient
from json import dumps


class ProductController:

    @staticmethod
    def update(request: dict, mqtt_client: MqttClient):

        store = 'ABC'
        corridor = 'G'
        column = 5
        row = 1
        display_id = 123

        product = Product(**request)
        display = f'{store}/{corridor}/{column}/{row}/{display_id}'

        mqtt_client.publish(
            topic=display,
            payload=dumps(product.to_dict())
        )

        return product.to_dict()
