''' 
Falta todo lo de get y post
'''

import logging
import routes
import settings

from controllers.display import DisplayController
from bottle import post, get, request, run
from services.mqtt_client import MqttClient, get_message

from controllers.product import ProductController

mqtt_client = MqttClient('tailor.cloudmqtt.com',"zbtbveka","3QAhOmlBfa90",18091,"/BajarInfoTag")


@get(routes.STATUS)
def status():
    return {
        'msg': 'Up and running',
        'version': settings.VERSION,
        'deployed at': settings.DEPLOYED_AT
    }


@post(routes.UPDATE_DISPLAY)
def update_display():
    return ProductController.update(location=DisplayController.verificate(request),request=request, mqtt_client=get_message)


def run_server():
    logging.info('Starting server.')
    run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    logging.info('Web Server Example Started')
    run_server()
