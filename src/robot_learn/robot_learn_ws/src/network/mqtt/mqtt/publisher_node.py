import rclpy
from rclpy.node import Node

class PublisherNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info(f"node {name} init...")

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode("mqtt_publisher_node")
    rclpy.spin(node)