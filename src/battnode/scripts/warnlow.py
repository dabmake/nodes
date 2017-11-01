#!/usr/bin/env python

import wiringpi2 as wpi
import rospy
import pygame
from std_msgs.msg import Int32

samplebefore = None

def callback(msg):
  global samplebefore
  print msg.data
  if msg.data < 2600 and samplebefore < 2600:
    pygame.mixer.music.play()
  samplebefore=msg.data


pygame.mixer.init(44100,-16,2,2048)
pygame.mixer.music.load("batterie.mp3")
     
rospy.init_node ('topic_subscriber')
sub = rospy.Subscriber('extbatterie', Int32, callback)
rospy.spin()
