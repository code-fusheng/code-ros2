import rclpy
from rclpy.node import Node
import paho.mqtt.client as Mqtt

class MqttTest(Node):
    def __init__(self, name):
        super().__init__(name)
        self.mqtt_client = Mqtt.Client()

        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message

        # connect to mqtt
        self.mqtt_client.connect("47.111.158.6", 1883, 60)
        # 
        self.mqtt_client.loop_start()


    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.get_logger().info("Connect to MQTT broker")
            # sub topic
            self.mqtt_client.subscribe("/patrol_robot/up/#") 
        else: 
            self.get_logger().error("Failed to connect to MQTT broker")
    
    def on_message(self, client, userdta, msg):
        self.get_logger().info("Received MQTT message: %s" % msg.payload.decode())

    def publish_message(self, msg):
        self.mqtt_client.publish("/patrol_robot/ros_debug", msg)

def main(args=None):
    rclpy.init(args=args)
    mqtt_test_node = MqttTest("mqtt_test_node")
    # pub mqtt msg
    mqtt_test_node.publish_message("hello! Ros MQTT!")
    rclpy.spin(mqtt_test_node)
    mqtt_test_node.destroy_node()
    rclpy.shutdown()




