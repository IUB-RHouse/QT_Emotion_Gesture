#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String
from qt_nuitrack_app.msg import Faces
from qt_robot_interface.srv import *
from qt_gesture_controller.srv import gesture_play

em_index = 1
async def sad_smile(em_index):
    if em_index == 0:
        emotionShow("QT/sad")
    elif em_index == 1:
        emotionShow("QT/calming_down")
async def gesture():
    gesturePlay("my_gesture", 0)
    
def smile_nod():
    gesturePlay_pub = rospy.Publisher('/qt_robot/gesture/play', String, queue_size=10)
    emotionShow_pub = rospy.Publisher('/qt_robot/emotion/show', String, queue_size=10)
    rospy.sleep(3.0)
    gesturePlay_pub.publish("my_gesture")
    emotionShow_pub.publish("QT/calming_down")

    
if __name__ == '__main__':
    rospy.init_node('my_tutorial_node')
    rospy.loginfo("my_tutorial_node started!")

    smile_nod()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

    rospy.loginfo("finsihed!")
