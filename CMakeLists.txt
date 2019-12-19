cmake_minimum_required(VERSION 2.8.3)
project(tuning_al_gui)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  tf
  geometry_msgs
  message_generation
  actionlib_msgs
  franka_gripper
  franka_msgs
  panda_pbd
)

catkin_python_setup()

catkin_package(
    INCLUDE_DIRS include
    CATKIN_DEPENDS roscpp rospy std_msgs message_runtime geometry_msgs actionlib_msgs panda_pbd
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${EIGEN3_INCLUDE_DIRS}
)

install(FILES plugin.xml
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
        )
