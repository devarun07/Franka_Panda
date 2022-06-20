#!/usr/bin/env python

import rospy
from franka_moveit import PandaMoveGroupInterface
import geometry_msgs.msg
import copy
import numpy as np

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


def create_demo_waypoints():
    waypoints = []
    x = list(np.linspace(0.5, 0.3, 500)) + list(np.linspace(0.3, 0.5, 500))
    y = list(np.linspace(-0.3, 0.3, 1000))
    #z = list(np.linspace(0.25, 0.4, 15)) + list(np.linspace(0.4, 0.25, 15))
    wpose = move_group.get_current_pose().pose

    for x_, y_ in zip(x, y):
        wpose.position.x = x_ 
        wpose.position.y = y_
        #wpose.position.z = z_
        waypoints.append(copy.deepcopy(wpose))

    (plan, fraction) = move_group.compute_cartesian_path(
        waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
    )  # jump_threshold

    # Note: We are just planning, not asking move_group to actually move the robot yet:
    return plan, fraction


def move_to_start_point():
    start_joint = [0.01609286626924037, 0.2271464286226975, -0.8959251844924626, -2.286066606840222, 0.24478825136039353, 2.4461594827969866, -0.34346179234818447]
    start_joint = [-0.186404176977863, 0.504819585016967, -0.439022758016959, -1.83051976289851, 0.289349729190495,	2.29955719127493, 0.062700418850548]
    move_group.go(start_joint, wait=True)
    move_group.stop()


if __name__ == "__main__":

    rospy.init_node("move_node") # initialise ros node
    move_group_interface = PandaMoveGroupInterface()
    move_group = getattr(move_group_interface, '_arm_group')

    move_to_start_point()
    new_plan, fraction = create_demo_waypoints()
    move_group.execute(new_plan, wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
