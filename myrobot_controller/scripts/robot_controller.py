#!/usr/bin/python3

import rospy
from std_msgs.msg import Float64

global received_data, pub1, pub2  # Declare the variable as global

def callback(data): #data is the content in "pub.publish"
    #rospy.loginfo(data.data)
    received_data = data.data 

    if(received_data==1.0):
        print("START")
        pub1.publish(3.0)
        pub2.publish(-3.0)
    
    elif(received_data==2.0):
        print("STOP")
        pub1.publish(0.0)
        pub2.publish(0.0)
    
    elif(received_data==3.0):
        print("TURN LEFT")
        pub1.publish(0.0)
        pub2.publish(-3.0)
    
    elif(received_data==4.0):
        print("TURN RIGHT")
        pub1.publish(3.0)
        pub2.publish(0.0)
def listener():
    rospy.init_node('listener')
    rospy.Subscriber("chatter", Float64, callback)

    rate = rospy.Rate(50)

    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    # pub1: left wheel
    # pub2: right wheel
    pub1 = rospy.Publisher("/my_diffbot/joint1_velocity_controller/command", Float64, queue_size=10)
    pub2 = rospy.Publisher("/my_diffbot/joint2_velocity_controller/command", Float64, queue_size=10)
    
    try:
        listener()
    except rospy.ROSInterruptException:
        pass