build:
	g++ first_ros2_node.cpp \
	-I /opt/ros/foxy/include/rclcpp/ \
	-I /opt/ros/foxy/include/rcl/ \
	-I /opt/ros/foxy/include/rcutils/ \
	-I /opt/ros/foxy/include/rmw \
	-I /opt/ros/foxy/include/rcl_yaml_param_parser/ \
	-I /opt/ros/foxy/include/rosidl_runtime_c \
	-I /opt/ros/foxy/include/rosidl_typesupport_interface \
	-I /opt/ros/foxy/include/rcpputils \
	-I /opt/ros/foxy/include/builtin_interfaces \
	-I /opt/ros/foxy/include/rosidl_runtime_cpp \
	-I /opt/ros/foxy/include/tracetools \
	-I /opt/ros/foxy/include/rcl_interfaces \
	-I /opt/ros/foxy/include/libstatistics_collector \
	-I /opt/ros/foxy/include/statistics_msgs \
	-L /opt/ros/foxy/lib/ \
	-lrclcpp -lrcutils \
	-o first_node
clean:
	rm first_node