#!/usr/bin/env python3
import sys
import cv2
from display import Display
import numpy as np


W = 2562//4
H = 1440//4

disp = Display(W, H)

class FeatureExtractor(object):
	GX = 16//2
	GY = 12//2

	def __init__(self):
		self.orb = cv2.ORB_create(100)

	def extract(self, img):
		feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)
		print(feats)
		return feats


fe = FeatureExtractor()

def process_frame(img):
	img = cv2.resize(img,(W,H))
	kp = fe.extract(img)

	for p in kp:
		u,v = map(lambda x: int(round(x)), p[0])
		cv2.circle(img, (u,v), color=(0,255,0), radius=3)

	disp.paint(img)

if __name__ == "__main__":
	cap = cv2.VideoCapture("test_video.mp4")

	while cap.isOpened():
		ret, frame = cap.read()
		if ret == True:
			process_frame(frame)
		else:
			break