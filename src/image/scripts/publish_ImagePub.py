#!/usr/bin/env python3

import rospy

import sys
import cv2
import os
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np

def start_node():
    rospy.init_node('image_pub')
    rospy.loginfo('image_pub node started')
    #cap = cv2.VideoCapture(0)
    cap = cv2.imread('/home/fsp/Downloads/vaca.jpeg')
    #success, img = cap.read()
    img = np.array(cap)
    print(img.shape)
    success = True
    bridge = CvBridge()
    imgMsg = bridge.cv2_to_imgmsg(img, "rgb8")
    pub = rospy.Publisher('image', Image, queue_size=10)
    while not rospy.is_shutdown():
        if success:
            #success, img = cap.read()
            #imgMsg = bridge.cv2_to_imgmsg(img, "rgb8")
            #cv2.imshow('image', img)
            #cv2.waitKey(1)
            pub.publish(imgMsg)
            rospy.Rate(60.0).sleep()
if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass