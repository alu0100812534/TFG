#! /usr/bin/env python2

import cv2
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import sys
import numpy as np
import StringIO
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from PIL import Image as other_img

options = Options()
options.add_argument('--headless')
print("[INFO] Loading Selenium Firefox webdriver...")

##### ROS PUBLISH
pub = rospy.Publisher('image_selenium', Image, queue_size=10)
rospy.init_node('selenium', anonymous=True)
rate = rospy.Rate(10) # 10hz

browser = webdriver.Firefox(firefox_options=options, executable_path="/home/daniel/catkin_ws/src/tfg/src/selenium/geckodriver")
browser.install_addon("/home/daniel/catkin_ws/src/tfg/src/selenium/adblock_plus-3.4.3.xpi", temporary=True) 
browser.get('https://www.youtube.com/watch?v=TgeX-AF7_DE?version=3&vq=hd720')
browser.maximize_window()

while(5<6):
	data = browser.get_screenshot_as_png()
	image = other_img.open(StringIO.StringIO(data))
	img_data=np.asarray(image)
	img_data = cv2.cvtColor(img_data, cv2.COLOR_RGBA2BGR)
	img_data = img_data[148:600, 36:870]


        pub.publish(CvBridge().cv2_to_imgmsg(img_data, "bgr8"))
        cv2.imshow("input", img_data)
	cv2.waitKey(10)


browser.quit()
