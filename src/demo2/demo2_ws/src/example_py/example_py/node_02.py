import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args) # 初始化 rclpy
    node = Node("node_02")  # 新建一个节点
    node.get_logger().info("hello i'm node_02. ")
    rclpy.spin(node) # 保持节点运行
    rclpy.shutdown()
