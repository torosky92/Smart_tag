import logging
import routes
import settings

from bottle import post, get, request, run
from services.mqtt_client import MqttClient

from controllers.product import ProductController

mqtt_client = MqttClient('localhost')


@get(routes.STATUS)
def status():
    return {
        'msg': 'Up and running',
        'version': settings.VERSION,
        'deployed at': settings.DEPLOYED_AT
    }

@get(routes.JOIN_USER)
def UserIn():
    return UserLogin.verificate(request=request.json)

@get(routes.REGISTER_USER)
def UserRegister():
    return UserLogin.addUser(request=request.json)

@post(routes.UPDATE_DISPLAY)
def update_display():
    return ProductController.update(request=request.json, mqtt_client=mqtt_client)


def run_server():
    logging.info('Starting server.')
    run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    logging.info('Web Server Example Started')
    run_server()
