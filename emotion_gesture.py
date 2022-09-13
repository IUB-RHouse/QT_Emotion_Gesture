#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String
from qt_nuitrack_app.msg import Faces
from qt_robot_interface.srv import *


def face_callback(msg):
    emotions = [msg.faces[0].emotion_angry, msg.faces[0].emotion_happy, msg.faces[0].emotion_surprise]
    em = max(emotions)
    em_index = emotions.index(em)
    if em_index == 0 and em >= 0.9:
        speech_pub.publish("It looks like you are angry! This is my angry face")
        emotionShow("QT/angry")
        rospy.sleep(2)
    elif em_index == 1 and em >= 0.9:
        speech_pub.publish("You are happy! This is my happy face")
        emotionShow("QT/happy")
        rospy.sleep(2)
    elif em_index == 2 and em >= 0.9:
        speech_pub.publish("This is surprising!")
        emotionShow("QT/surprise")
        rospy.sleep(2)
    
    
if __name__ == '__main__':
    rospy.init_node('my_tutorial_node')
    rospy.loginfo("my_tutorial_node started!")

    emotionShow = rospy.ServiceProxy('/qt_robot/emotion/show', emotion_show)
    speech_pub = rospy.Publisher('/qt_robot/speech/say', String, queue_size=1)

    # define ros subscriber
    rospy.Subscriber('/qt_nuitrack_app/faces', Faces, face_callback)
   
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

    rospy.loginfo("finsihed!")
