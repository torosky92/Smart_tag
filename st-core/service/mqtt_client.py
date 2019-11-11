from paho.mqtt.client import Client

class MqttClient(Client):
    def _init_(self, broker: str, port: int = 1883):
        super()._init_()
        self.connect(broker,port)
    
    