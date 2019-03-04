#!/usr/bin/env python
import cv2
import rospy
import numpy as np
import argparse
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import time
import datetime

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
    "sofa", "train", "tvmonitor"]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe("/home/daniel/catkin_ws/src/tfg/src/opencv_cam/MobileNetSSD_deploy.prototxt.txt", "/home/daniel/catkin_ws/src/tfg/src/opencv_cam/MobileNetSSD_deploy.caffemodel")

 #db
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                      user="root",         # your username
                      passwd="",  # your password
                      db="tfg_record",
                      autocommit=True)        # name of the data base

lastime = -1
out = None
source = -1
cur = db.cursor()

def callback(data):
    try:
        cap = CvBridge().imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
        print(e)
        out.release()

    Cnn(cap)


def Cnn(image):
        global lastime
        global out
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

        # ps pass the blob through the network and obtain the detections and
        # predictions
        print("[INFO] computing object detections...")
        net.setInput(blob)
        detections = net.forward()
        pub = rospy.Publisher('net_topic', Image, queue_size=10)

        # loop over the detections
        for i in np.arange(0, detections.shape[2]):
            # extract the confidence (i.e., probability) associated with the
            # prediction
            confidence = detections[0, 0, i, 2]
            # out = None
            # filter out weak detections by ensuring the `confidence` is
            # greater than the minimum confidence
            if confidence > 0.50:
                # extract the index of the class label from the `detections`,
                # then compute the (x, y)-coordinates of the bounding box for
                # the object
                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # display the prediction
                label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
                print("[INFO] {}".format(label))
                cv2.rectangle(image, (startX, startY), (endX, endY),
                    COLORS[idx], 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(image, label, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)


                if idx == 15 :
                    if ((time.time() * 1000) - lastime) > 5000:
                        cur.execute("INSERT INTO log (`time`, `message`, `source`, `type`) VALUES ('"+time.strftime('%Y-%m-%d %H:%M:%S')+"', 'Ha entrado una persona!', "+str(source)+",'0')")
                        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
                        out = cv2.VideoWriter('/opt/lampp/htdocs/tfg/record_videos/'+str(time.strftime('%Y-%m-%d %H:%M:%S'))+'.mp4',fourcc, 20.0, (w,h))
                        print out
                    lastime = time.time() * 1000
                    out.write(image)
                    rospy.loginfo('escribiendo imagen...')

                    k = cv2.waitKey(33)
                    if k == 27:    # Esc key to stop
                        break


        if ((time.time() * 1000) - lastime) > 5000  and lastime >= 0 :
            cur.execute("INSERT INTO log (`time`, `message`, `source`, `type`) VALUES ('"+time.strftime('%Y-%m-%d %H:%M:%S')+"', 'Ha salido una persona!', "+str(source)+",'1')")
            lastime = -1
            out.release()


        # show the output image
        cv2.imshow("Output", image)
        pub.publish(CvBridge().cv2_to_imgmsg(image, "bgr8"))
        cv2.waitKey(1)

rospy.init_node('listener', anonymous=True)
source = rospy.get_param("~source", -1)

rospy.Subscriber("image_ch",Image, callback)
rospy.spin()
