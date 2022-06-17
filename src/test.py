import rospy
# from panda_robot import PandaArm
from franka_moveit import PandaMoveGroupInterface
from math import pi, tau, dist, fabs, cos
import geometry_msgs.msg
import time
from moveit_commander.conversions import pose_to_list
import copy


rospy.init_node("panda_demo") # initialise ros node
move_group_interface = PandaMoveGroupInterface()
move_group = getattr(move_group_interface, '_arm_group')

print(type(move_group))


#rosrun rqt_controller_manager rqt_controller_manager 


print("here")
# joint_goal = move_group.get_current_joint_values()
# print(joint_goal)
# move_group_interface.move_to_neutral()

# start_joint = [0.040492694824934006, 0.040492694824934006, 2.8187033503834162, 0.5386136185746444, -2.8851618513822377, -2.218324976435879, 0.13659428085221184]
# start_joint = [-1.380531998707737e-05, -0.7847858029411255, -0.00026834713815907505, -2.35646303223727, -0.0005735719580126927, 1.5713429098659086, 0.785576719562188]
# start_joint = [0.015418365841958217, -0.01468125086331555, 0.008743297412849958, -1.3793302623519712, 0.014338668302529386, 1.5502972790957368, 0.973981623770462]
# start_joint = [k+0.2 for k in start_joint]
# move_group.go(start_joint, wait=True)
# move_group.stop()


# start_joint = [0.01609286626924037, 0.2271464286226975, -0.8959251844924626, -2.286066606840222, 0.24478825136039353, 2.4461594827969866, -0.34346179234818447]

# move_group.go(start_joint, wait=True)
# move_group.stop()


# # plan  = move_group.plan(start_joint)
# move_group.go(start_joint, wait=True)
# move_group.stop()



# joint_goal = move_group.get_current_joint_values()
# print(joint_goal)
# # joint_goal = [-1.380531998707737e-05, -0.7847858029411255, -0.00026834713815907505, -2.35646303223727, -0.0005735719580126927, 1.5713429098659086, 0.785576719562188]
# joint_goal = [k+0.05 for k in joint_goal]
# move_group.go(joint_goal, wait=True)
# move_group.stop()

# print(move_group.get_current_pose().pose)
def create_waypoints(scale):
    waypoints = []

    wpose = move_group.get_current_pose().pose
    wpose.position.z += scale * 0.1  # First move up (z)
    wpose.position.y += scale * 0.2  # and sideways (y)
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.x += scale * -0.1  # Second move forward/backwards in (x)
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.y -= scale * 0.1  # Third move sideways (y)
    waypoints.append(copy.deepcopy(wpose))

    (plan, fraction) = move_group.compute_cartesian_path(
        waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
    )  # jump_threshold

    # Note: We are just planning, not asking move_group to actually move the robot yet:
    return plan, fraction


new_plan, fraction = create_waypoints(0.1)
print(type(new_plan))
move_group.execute(new_plan, wait=True)
move_group.stop()
move_group.clear_pose_targets()

# for _ in range(3):
#     joint_goal = move_group.get_current_joint_values()
#     joint_goal = [k+0.2 for k in joint_goal]
#     move_group.go(joint_goal, wait=True)
#     move_group.stop()
#     move_group.clear_pose_targets()
#     time.sleep(3)


# move_group.go(joint_goal, wait=True)
# move_group.stop()

# print(move_group.get_current_pose().pose)
# pose_goal = geometry_msgs.msg.Pose()
# pose_goal.orientation.w = 0
# pose_goal.position.x = 0.4
# pose_goal.position.y = -0.25
# pose_goal.position.z = 0.4

# move_group.set_pose_target(pose_goal)
# plan = move_group.go(wait=True)
# move_group.clear_pose_targets()
# print(move_group.get_current_pose().pose)


#r = PandaArm() # create PandaArm instance

# r.move_to_neutral() # moves robot to neutral pose; uses moveit if available, else JointTrajectory action client

# pos,ori = r.ee_pose() # get current end-effector pose (3d position and orientation quaternion of end-effector frame in base frame)
# print(pos)

# r.get_gripper().home_joints() # homes gripper joints
#r.get_gripper().close() # open gripper

# # # r.move_to_joint_position([-8.48556818e-02, -8.88127666e-02, -6.59622769e-01, -1.57569726e+00, -4.82374882e-04,  2.15975946e+00,  4.36766917e-01]) # move robot to the specified pose
# r.move_to_joint_position([1.7105467670131145, 0.21580206177109165, -1.8450747339265565, -1.6647906301398026, 0.26817784990204707, 1.8585665604803296, 0.9557275336203386])

# pos = [1.48963375, -0.17584198,  1.4870016]

# r.move_to_cartesian_pose(pos,ori) # mov




# joint_goal = move_group.get_current_joint_values()
# print(joint_goal)

# joint_goal[0] = 0
# joint_goal[1] = -tau / 4
# joint_goal[2] = 0
# joint_goal[3] = -tau / 6
# joint_goal[4] = 0
# joint_goal[5] = tau / 4  # 1/6 of a turn
# joint_goal[6] = 0

# move_group.go(joint_goal, wait=True)
# move_group.stop()