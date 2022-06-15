import rospy
from franka_core_msgs.msg import JointCommand


joint_command_publisher = rospy.Publisher(
                'franka_ros_interface/motion_controller/arm/joint_commands',
                JointCommand,
                tcp_nodelay=True,
                queue_size=1)


if __name__ == '__main__':
    rospy.init_node('test_fri')

    _command_msg = JointCommand()
    _joint_names = ['panda_finger_joint1', 'panda_finger_joint2', 'panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5', 'panda_joint6', 'panda_joint7']
    _command_msg.names = _joint_names
    _command_msg.position = [0.009883818216621876, 0.009883818216621876, 1.7105467670131145, 0.21580206177109165, -2.8450747339265565, -1.6647906301398026, 0.56817784990204707, 1.2485665604803296, 0.9557275336203386]
    _command_msg.mode = JointCommand.POSITION_MODE
    _command_msg.header.stamp = rospy.Time.now()
    joint_command_publisher.publish(_command_msg)


    # apt install ros-noetic-gazebo-ros-control ros-noetic-rospy-message-converter ros-noetic-effort-controllers ros-noetic-joint-state-controller ros-noetic-moveit ros-noetic-moveit-commander ros-noetic-moveit-visual-tools