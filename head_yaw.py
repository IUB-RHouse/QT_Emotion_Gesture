#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import JointState

head_yaw_pos = 0
rospy.init_node('my_tutorial_node')
rospy.loginfo("my_tutorial_node started!")

head_pub = rospy.Publisher('/qt_robot/head_position/command', Float64MultiArray, queue_size=10)
rospy.sleep(3.0)

def state_callback(msg):
    global head_yaw_pos
    head_yaw_pos = msg.position[msg.name.index("HeadYaw")]

rospy.Subscriber('/qt_robot/joints/state', JointState, state_callback)

if __name__ == '__main__':
    head_yaw_ref = 15.0
    while not rospy.is_shutdown():
        try:
            href = Float64MultiArray()
            href.data = [head_yaw_ref, 0]
            head_pub.publish(href)
            rospy.sleep(4)
            rospy.loginfo("Current position : %.2f" ,head_yaw_pos)
            head_yaw_ref = -15 if head_yaw_ref == 15 else 15
        except KeyboardInterrupt:
            pass
    rospy.loginfo("finsihed!")
