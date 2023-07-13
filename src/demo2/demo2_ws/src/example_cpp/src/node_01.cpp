#include "rclcpp/rclcpp.hpp"

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<rclcpp::Node>("node_01");
    RCLCPP_INFO(node -> get_logger(), "node_01 节点已经启动.");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}