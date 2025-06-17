
"""
@file features.py

@brief This module contains feature extraction functions for analyzing leaf images.
      It focuses on extracting color histogram features in HSV color space,
      which are used for classifying plant health status.

@author Macy Varga
"""

# cv2: OpenCV, used to convert color spaces and compute histograms
import cv2
# numpy: For handling and manipulating arrays (like histogram data)
import numpy as np
# The fuction extract_color_features takes on parameter ::image: an image (in BGR
# format as loaded by OpenCV)
def extract_color_features(image):
   # Converts the image from BGR (default in OpenCV) to HSV
   hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
   # Computes histograms for each HSV channel. These histograms describe the
   # distribution of colors in the image
   hist_h = cv2.calcHist([hsv], [0], None, [50], [0, 180])
   hist_s = cv2.calcHist([hsv], [1], None, [60], [0, 256])
   hist_v = cv2.calcHist([hsv], [2], None, [60], [0, 256])
   # Merges the 3 histograms into one long feature vector
   # flatten() turns the 2D arrays into a 1D array
   hist = np.concatenate([hist_h, hist_s, hist_v]).flatten()
   # Normalizes the histogram so that it’s scale-independent. nsures all
   # values sum to 1, turning it into a probability distribution
   hist = hist / np.sum(hist)
   return hist
