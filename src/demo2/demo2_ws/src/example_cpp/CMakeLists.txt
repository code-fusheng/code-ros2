cmake_minimum_required(VERSION 3.5)
project(example_cpp)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

# 在CmakeLists.txt最后一行加入下面两行代码 添加这两行代码的目的是让编译器编译node_01这个文件
add_executable(node_01 src/node_01.cpp)
ament_target_dependencies(node_01 rclcpp)
add_executable(node_03 src/node_03.cpp)
ament_target_dependencies(node_03 rclcpp)
# 接着在上面两行代码下面添加下面的代码
install(TARGETS
  node_01
  node_03
  DESTINATION lib/${PROJECT_NAME}
)


