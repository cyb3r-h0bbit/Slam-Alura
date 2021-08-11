#!/usr/bin/env python3
import cv2

def process_frame(img):
	img = cv2.resize(img,(1920//2, 1080//2))
	print(img.shape)

if __name__ == "__main__":
	cap = cv2.VideoCapture("test_video.mp4")

	while cap.isOpened():
		ret, frame = cap.read()
		if ret == True:
			process_frame(frame)
		else:
			break