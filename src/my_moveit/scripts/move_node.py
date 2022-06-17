#!/usr/bin/env python

import rospy
from franka_moveit import PandaMoveGroupInterface
import geometry_msgs.msg
import copy



if __name__ == "__main__":

    rospy.init_node("move_node") # initialise ros node
    move_group_interface = PandaMoveGroupInterface()
    move_group = getattr(move_group_interface, '_arm_group')


    def create_waypoints(scale):
        waypoints = []

        wpose = move_group.get_current_pose().pose
        wpose.position.z += scale * 0.1  # First move up (z)
        wpose.position.y += scale * 0.2  # and sideways (y)
        waypoints.append(copy.deepcopy(wpose))

        wpose.position.x += scale * 0.1  # Second move forward/backwards in (x)
        waypoints.append(copy.deepcopy(wpose))

        wpose.position.y -= scale * 0.1  # Third move sideways (y)
        waypoints.append(copy.deepcopy(wpose))

        (plan, fraction) = move_group.compute_cartesian_path(
            waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
        )  # jump_threshold

        # Note: We are just planning, not asking move_group to actually move the robot yet:
        return plan, fraction


    new_plan, fraction = create_waypoints(0.2)
    move_group.execute(new_plan, wait=True)
    move_group.stop()
    move_group.clear_pose_targets()