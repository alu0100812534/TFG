#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""

Copyright (c) 2015 PAL Robotics SL.
Released under the BSD License.

Created on 7/14/15

@author: Sammy Pfeiffer

webcam.py contains
a testing code to see if opencv can open a video stream
useful to debug if video_stream does not work
"""

import cv2
import sys
import rospy 
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "You must give an argument to open a video stream."
        print "  It can be a number as video device, e.g.: 0 would be /dev/video0"
        print "  It can be a url of a stream,        e.g.: rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov"
        print "  It can be a video file,             e.g.: myvideo.mkv"
        exit(0)

    resource = sys.argv[1]
    # If we are given just a number, interpret it as a video device
    if len(resource) < 3:
        resource_name = "/dev/video" + resource
        resource = int(resource)
    else:
        resource_name = resource
    print "Trying to open resource: " + resource_name
    cap = cv2.VideoCapture(resource)
    if not cap.isOpened():
        print "Error opening resource: " + str(resource)
        print "Maybe opencv VideoCapture can't open it"
        exit(0)
    print "Correctly opened resource, starting to show feed."

##### ROS PUBLISH
    pub = rospy.Publisher('image_ch', Image, queue_size=10)
    rospy.init_node('open_cam', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
  ############
    rval, frame = cap.read()
    while rval:
        rval, frame = cap.read()
        key = cv2.waitKey(1)
        pub.publish(CvBridge().cv2_to_imgmsg(frame, "bgr8"))
        
        # print "key pressed: " + str(key)
        # exit on ESC, you may want to uncomment the print to know which key is ESC for you
        if key == 27 or key == 1048603:
            break
    cv2.destroyWindow("preview")
