"""
@file spot_detection.py

@brief Provides functions for detecting diseased spots on leaves using HSV thresholding
      and contour detection with OpenCV.

@function detect_spots
   Identifies spot regions in an HSV image and returns their properties for analysis.

@returns
   Tuple (spot_data, mask) where spot_data includes area and mean color per spot.

@author
   Macy Varga
"""

# cv2: OpenCV – used for color filtering, contour detection, and image manipulation
import cv2
# numpy: Used to create arrays for masking and thresholding operations
import numpy as np

# The function detect_spots expects an HSV image as input (from preprocess.py).
# Detect and analyze regions of interest (sick spots)
def detect_spots(hsv_image):
   # Defines the HSV color range for detecting typical sick spot colors
   # (e.g., brown or dark yellow). lower and upper bounds are used in color
   # segmentation.
   lower = np.array([0, 40, 20])
   upper = np.array([30, 255, 200])
   # Uses OpenCV to create a binary mask: Pixels within the HSV range are turned white
   # (255), everything else is black (0).
   mask = cv2.inRange(hsv_image, lower, upper)
   # Finds the external contours in the binary mask (i.e., outlines of spots).
   # contours will be a list of spot boundaries
   contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   # Prepares a list to store details about each detected spot: area, color, contour shape
   spot_data = []

   # Calculates the area of each detected contour. Ignores very small regions (likely noise)
   # using a threshold of 100 pixels
   for cnt in contours:
       area = cv2.contourArea(cnt)
       if area > 100:
           # Creates a blank mask the same size as the image.Draws the current contour
           # (cnt) onto this mask.This isolates the region for color analysis.
           mask_single = np.zeros(hsv_image.shape[:2], dtype=np.uint8)
           cv2.drawContours(mask_single, [cnt], -1, 255, -1)
           # Computes the mean HSV color of the region defined by the contour
           mean_val = cv2.mean(hsv_image, mask=mask_single)
           # Adds a dictionay
           spot_data.append({
               'area': area,
               'mean_color': mean_val,
               'contour': cnt
           })
   # spot_data: list of detected spots with color and size info. mask: the
   # original binary mask (useful for visualization or debugging)
   return spot_data, mask
