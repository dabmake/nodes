#!/usr/bin/env python

import wiringpi2 as wpi
import rospy
from std_msgs.msg import Int32

rospy.init_node('topic_publisher')
pub = rospy.Publisher('extbatterie', Int32)
rate = rospy.Rate(1)
wpi.wiringPiSetupSys()

while not rospy.is_shutdown():
  
  adcValue = wpi.analogRead(0)
  print adcValue
  pub.publish(adcValue)
  rate.sleep()
