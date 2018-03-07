import numpy as np
import cv2
from imutils.object_detection import non_max_suppression
from imutils import paths
import imutils

cap = cv2.VideoCapture('video_340.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    orig = frame.copy()
   #    cv2.imshow('frame',frame)

	# detect people in the image
    (rects, weights) = hog.detectMultiScale(frame, winStride = (8,8), padding = (32,32), scale = 1.05)

  # draw the original bounding boxes
    for (x,y,w,h) in rects:
        cv2.rectangle(orig, (x,y), (x + w, y + h), (0,0,255), 2)

    # apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs = None, overlapThresh=0.65)

	# draw the final bounding boxes
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

	# show the output images
	cv2.imshow("Before NMS", orig)
	cv2.imshow("After NMS", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
