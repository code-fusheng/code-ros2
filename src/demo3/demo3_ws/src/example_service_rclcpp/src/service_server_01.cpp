#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"

class ServiceServer01 : public rclcpp::Node {
    public:
        ServiceServer01(std::string name) : Node(name) {
            RCLCPP_INFO(this->get_logger(), "Node %s Is Started.", name.c_str());
        }
    private:
        rclcpp::Service<example_interfaces::srv::AddTwoInts>::SharedPtr add_ints_server_;
        void handle_add_two_ints(
            const std::shared_ptr<example_interfaces::srv::AddTwoInts::Request> request,
            std::shared_ptr<example_interfaces::srv::AddTwoInts::Response> response) {
            RCLCPP_INFO(this->get_logger(), "收到a: %ld b: %ld", request->a,
                request->b);
            response->sum = request->a + request->b;
  };
};

int main(int argc, char** argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<ServiceServer01>("service_server_01");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}