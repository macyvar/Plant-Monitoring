"""
@file preprocess.py

@brief Contains preprocessing utilities for leaf image analysis, including resizing,
      color space conversion, and image blurring to prepare for further analysis.

@function preprocess_image
   Loads an image, resizes it, converts it to HSV color space,
   and applies Gaussian blur to reduce noise.

@returns
   Tuple (original_image, blurred_hsv_image)

@author
   Macy Varga
"""

# cv2 is the OpenCV library used for image processing. Used to load,
# resize, convert, and blur images
import cv2

# The function preprocess_image takes 2 params:: image_path: the full
# file path of the image to process and resize_dim: optional argument
# for the new image size, default is 256×256 pixels
def preprocess_image(image_path, resize_dim=(256, 256)):
   # Uses cv2.imread() to load the image from disk in BGR format
   image = cv2.imread(image_path)
   # Resizes the image to 256×256 (or to whatever size is passed in)
   image = cv2.resize(image, resize_dim)
   # Converts the image from BGR to HSV (Hue, Saturation, Value)
   hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
   # Applies a Gaussian blur to reduce noise and small image artifacts.
   # Kernel size (5, 5) smooths the image while preserving larger structures like spots
   blurred = cv2.GaussianBlur(hsv, (5, 5), 0)
   return image, blurred
