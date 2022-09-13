#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('my_tutorial_node')
    rospy.loginfo("my_tutorial_node started!")

    # creating a ros publisher
    speechSay_pub = rospy.Publisher('/qt_robot/speech/say', String, queue_size=10)
    rospy.sleep(3.0)

    # publish a text message to TTS
    speechSay_pub.publish("Hello! my name is QT!")

    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

    rospy.loginfo("finsihed!")
