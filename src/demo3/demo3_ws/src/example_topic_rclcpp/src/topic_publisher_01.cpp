#include "rclcpp/rclcpp.hpp"
// 导入消息 +新增
#include "std_msgs/msg/string.hpp"

class TopicPublisher01 : public rclcpp :: Node
{
    public:
        TopicPublisher01(std::string name) : Node(name)
        {
            RCLCPP_INFO(this -> get_logger(), "%s 节点已经启动.", name.c_str());
            // 创建发布者
            command_publisher_ = this -> create_publisher<std_msgs::msg::String>("command", 10);
            // 创建定时器 500ms 周期发布
            timer_ = this -> create_wall_timer(std::chrono::milliseconds(500), std::bind(&TopicPublisher01::timer_callback, this));
        }
    private:
        // 声明话题发布者 
        rclcpp::Publisher<std_msgs::msg::String>::SharedPtr command_publisher_;
        // 声明定时器指针
        rclcpp::TimerBase::SharedPtr timer_;
        // 回调函数
        void timer_callback()
        {
            // 创建消息
            std_msgs::msg::String message;
            message.data = "forward";
            // 日志打印
            RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
            // 发布消息
            command_publisher_->publish(message);
        }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<TopicPublisher01>("topic_publisher_01");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}