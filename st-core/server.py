''' 
Falta todo lo de get y post
'''
import bottle
from bottle import post, get, request, run

import logging
import routes
import settings

from services.mqtt_client import MqttClient, get_message
from controllers.product import ProductController
from controllers.display import DisplayController
from controllers.Users import UserController

mqtt_client = MqttClient(SERVER_MQTT,USER_MQTT,PASSWORD_MQTT,PORT_MQTT,TAG_MQTT)

@get(routes.BASE)
def index():
    return "Index!"

@get(routes.STATUS)
def status():
    return {
        'msg': 'Up and running',
        'version': settings.VERSION,
        'deployed at': settings.DEPLOYED_AT
    }

@get(routes.MESSAGE_MQTT)
def message_mqtt():
    return ProductController.updateQuantity(get_message)

@post(routes.UPDATE_DISPLAY)
def update_display():
    return DisplayController.update(request=request, mqtt_client=mqtt_client)

@post(routes.VERIFICATE_DISPLAY)
def verificate_display():
    return DisplayController.verificate(request=request)

@post(routes.UPDATE_PRODUCT)
def update_product():
    return ProductController.update(request=request)

@post(routes.VERIFICATE_USER)
def verificate_user():
    return UserController.verificate(request=request)

@post(routes.DELETE_USER)
def delete_user():
    return UserController.delete(request=request)

@post(routes.UPDATE_USER)
def update_user():
    return UserController.update(request=request)

def run_server():
    logging.info('Starting server.')
    run(host='localhost', port=8080, debug=True)


if __name__ == '__main__':
    logging.info('Web Server Example Started')
    run_server()
