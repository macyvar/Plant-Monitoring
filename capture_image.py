"""
@file capture_image.py

@brief This file is used for capturing leaf images on the Raspberry Pi using the Camera Module 3.
      Images are saved to an external SSD for further processing.

@author Macy Varga
"""

import os
import time
from datetime import datetime
from picamera2 import Picamera2, Picamera2Error

# Path to the SSD mount
SSD_PATH = "/media/ssd"
SAVE_FOLDER = "leaf_images"

# Full path where images will be stored
save_dir = os.path.join(SSD_PATH, SAVE_FOLDER)

# Create directory if it doesn't exist
try:
   os.makedirs(save_dir, exist_ok=True)
except Exception as e:
   print(f"Error creating directory {save_dir}: {e}")
   exit(1)


# Generate a timestamped filename
timestamp = datetime.now().strftime("leaf_%Y%m%d_%H%M%S.jpg")
image_path = os.path.join(save_dir, timestamp)

# Initialize and capture an image
try:
   print("Starting camera...")
   picam2 = Picamera2()
   picam2.start()
   time.sleep(2)  # Allow camera to warm up
   picam2.capture_file(image_path)
   print(f"Image saved to: {image_path}")
except Picamera2Error as cam_err:
   print(f"Camera error: {cam_err}")
except Exception as err:
   print(f"Unexpected error: {err}")


"""
On Rasberry Pi, not Mac:
1. Enble camera with:
   " sudo raspi-config "
   meaning: Interface Options > Camera > Enable
2. Install the camera library:
   " sudo apt update "
   " sudo apt install python3-picamera2 "
3. Make sure your SSD is mounted at /media/ssd
   # Use " lsblk " or " df -h " to confirm and change SSD_PATH if needed.

To run: ON THE PI
   " python3 capture_leaf_image.py "
"""
