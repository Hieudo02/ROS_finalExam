#!/usr/bin/python3

import rospy
from std_msgs.msg import String

def callback(data): #data is the content in "pub.publish"
    rospy.loginfo(rospy.get_caller_id() + "i heard %s", data.data)
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()
    
if __name__ == '__main__':
    listener()
