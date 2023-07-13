#include "rclcpp/rclcpp.hpp"

class ServiceServer01 : public rclcpp::Node {
    public:
        ServiceServer01(std::string name) : Node(name) {
            RCLCPP_INFO(this->get_logger(), "Node %s Is Started.", name.c_str());
        }
    private:
};

int main(int argc, char** argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<ServiceServer01>("service_server_01");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}