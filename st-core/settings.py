import os
import datetime as dt

APP_NAME = os.getenv('APP_NAME', 'st-core')

COUNTRY = os.getenv('COUNTRY')
VERSION = '0.0.0'

BASE_PATH = os.getenv('BASE_PATH', '')

DEBUG = os.getenv('DEBUG', False)
DEPLOYED_AT = dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

SERVER_MQTT = 'tailor.cloudmqtt.com'
USER_MQTT = "zbtbveka"
PASSWORD_MQTT = "3QAhOmlBfa90"
PORT_MQTT = 18091
TAG_MQTT = "/BajarInfoTag"