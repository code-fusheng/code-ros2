import rclpy
from rclpy.node import Node

class SubscriberNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info(f"node {name} init...")

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode("mqtt_subscriber_node")
    rclpy.spin(node)

