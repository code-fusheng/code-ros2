#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class Node04(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("大家好,我是%s!" % name)
    
def main(args=None):
    rclpy.init(args=args) # 初始化 rcply
    node = Node04("node_04")
    rclpy.spin(node)
    rclpy.shutdown()