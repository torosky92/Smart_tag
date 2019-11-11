from paho.mqtt.client import Client


class MqttClient(Client):
    def __init__(self, broker: str, port: int = 1883):
        super().__init__()
        self.connect(broker, port)
