#!/usr/bin/env python3
import sys
import cv2
from display import Display


W = 2562//4
H = 1440//4



disp = Display(W, H)
orb = cv2.ORB()

def process_frame(img):
	kp1, des1 = orb.detectAndCompute(img,None)
	img = cv2.resize(img,(W,H))
	disp.paint(img)

if __name__ == "__main__":
	cap = cv2.VideoCapture("test_video.mp4")

	while cap.isOpened():
		ret, frame = cap.read()
		if ret == True:
			process_frame(frame)
		else:
			break