# USAGE
# python deep_learning_object_detection.py --image images/example_01.jpg \
#	--prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel

# import the necessary packages
import numpy as np
import argparse
import cv2
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PIL import Image
import StringIO
import threading

CONFIDENCE = 0.20

# SELENIUM
i = 5
a = 0
options = Options()
options.add_argument('--headless')
print("[INFO] Loading Selenium Firefox webdriver...")
browser = webdriver.Firefox(firefox_options=options, executable_path="/usr/local/bin/geckodriver")
browser.get('https://www.youtube.com/watch?v=XalgyWjBSsk')
browser.maximize_window()
#####

# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")

# load the input image and construct an input blob for the image
# by resizing to a fixed 300x300 pixels and then normalizing it
# (note: normalization is done via the authors of the MobileNet SSD
# implementation)
a = 0;
while 5<6:

	data = browser.get_screenshot_as_png()
	image = Image.open(StringIO.StringIO(data))
	a += 1
	img_data=np.asarray(image)
	img_data = cv2.cvtColor(img_data, cv2.COLOR_RGBA2BGR)
	img_data = img_data[148:600, 36:870]
	(h, w) = img_data.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(img_data, (300, 300)), 0.007843, (300, 300), 127.5)

	# pass the blob through the network and obtain the detections and
	# predictions
	print("[INFO] computing object detections...")
	net.setInput(blob)
	detections = net.forward()

	# loop over the detections
	for i in np.arange(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with the
		# prediction
		confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
		if confidence > CONFIDENCE:
			# extract the index of the class label from the `detections`,
			# then compute the (x, y)-coordinates of the bounding box for
			# the object
			idx = int(detections[0, 0, i, 1])
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")
                        if CLASSES[idx] == "person":
			# display the prediction
				label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
				print("[INFO] {}".format(label))
				cv2.rectangle(img_data, (startX, startY), (endX, endY),
					COLORS[idx], 2)
				y = startY - 15 if startY - 15 > 15 else startY + 15
				cv2.putText(img_data, label, (startX, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
		    # show the output image
	        cv2.imshow("input", img_data)
	        cv2.waitKey(10)

browser.quit()
