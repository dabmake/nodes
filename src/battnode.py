#!/usr/bin/python

import wiringpi2 as wpi
import rospy
from st_msgs.msg import Int32

rospy.init_node('topic_publisher')
pub = rospy.Publisher('batterie', Int32)
rate = rospy.Rate(1)

while not rospy.is_shutdown()
  wpi.wiringPiSetupSys()
  adcValue = wpi.analogRead(0)
  #print adcValue
  pub.publish(adcValue)
  rate.sleep()
