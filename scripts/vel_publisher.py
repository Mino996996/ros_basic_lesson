#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('vel_publisher')
pub = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10 )
while not rospy.is_shutdown():
  vel = Twist()
  direction = raw_input('f: forward, b: backword, l: left, r: right > ')
  if 'f' in direction:
    vel.liner.x = 0.5
  if 'b' in direction:
    vel.liner.x = -0.5
  if 'l' in direction:
    vel.angular.z = 1.0
  if 'f' in direction:
    vel.angular.z = -1.0
  if 'q' in direction:
    break
  print vel
  pub.publish(vel)    