from paho.mqtt.client import Client
import urllib.parse as urlparse

def get_message(mosq, obj, msg):
    return(msg.payload)


class MqttClient(Client):
    def __init__(
        self,
        mqttServer: str,
        mqttuser: str,
        mqttpassword: str,
        mqttPort: int,
        mqttTag: str
    ):
        super().__init__()        
        self.on_message = get_message
        self.username_pw_set(mqttuser, mqttpassword)
        self.connect(mqttServer, mqttPort, 60, '')
        self.loop_start()
        self.subscribe (mqttTag ,0 )
    
    def sendMqtt(self, mqttSendTag:str, mqttSendList: str):
        print(mqttSendList)
        self.publish ( mqttSendTag, mqttSendList)

    