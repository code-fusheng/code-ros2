import rclpy
from rclpy.node import Node
import paho.mqtt.client as Mqtt

class MqttClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = Mqtt.Client()

    # connect
    def connect(self):
        self.client.connect(self.host, self.port)
        self.client.loop_start()

    # disconnect
    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

    # 
    def on_connect(self, client, userdata, flags, rc):
        print("MQTT connected with result code: " + str(rc))

    # 
    def on_message(self, client, userdata, msg):
        print("Received MQTT message: " + msg.payload.decode())    