from models.Users import Users
from services.mqtt_client import MqttClient
from json import dumps


class UserController:

    @staticmethod
    def verificate(request: dict):
        users = Users(**request)
        return Users.to_dict()
    
    def addUser(request: dict):
        users = Users(**request)
        return Users.to_dict()
