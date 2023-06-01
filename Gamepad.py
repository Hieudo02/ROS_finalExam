#!/usr/bin/python3

import rospy
from std_msgs.msg import Float64
import RPi.GPIO as GPIO

BUTTON_GPIO = [17, 27, 22, 23]

if __name__ == '__main__':
    rospy.init_node('talker', anonymous=True)

    pub = rospy.Publisher('chatter', Float64, queue_size = 10)

    GPIO.setmode(GPIO.BCM)
    for i in BUTTON_GPIO:
        GPIO.setup(i, GPIO.IN)
        GPIO.setup(i, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    rate = rospy.Rate(50)

    while not rospy.is_shutdown():
        if(GPIO.input(BUTTON_GPIO[0]) == 1):
            print("START")
            gpio_state = 1.0 
            rospy.loginfo(gpio_state)
            pub.publish(gpio_state)
        
        elif(GPIO.input(BUTTON_GPIO[1]) == 1):
            print("STOP")
            gpio_state = 2.0 
            rospy.loginfo(gpio_state)
            pub.publish(gpio_state)
        
        elif(GPIO.input(BUTTON_GPIO[2]) == 1):
            print("TURN LEFT")
            gpio_state = 3.0 
            rospy.loginfo(gpio_state)
            pub.publish(gpio_state)

        elif(GPIO.input(BUTTON_GPIO[3]) == 1):
            print("TURN LEFT")
            gpio_state = 4.0 
            rospy.loginfo(gpio_state)
            pub.publish(gpio_state)
        
        #rate.sleep()  

    GPIO.cleanup()
