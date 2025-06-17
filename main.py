"""
@file main.py

@brief This is the main script that integrates preprocessing, feature extraction,
      spot detection, and machine learning classification for plant disease detection.
      It loads a trained model, processes a given leaf image, extracts features,
      predicts whether the leaf is diseased, and counts visible disease spots.

@usage
   python3 main.py

@dependencies
   - preprocess.py
   - spot_detection.py
   - features.py
   - train_classifier.py
   - model.pkl (pre-trained Random Forest model)

@author
   Macy Varga
"""

# preprocess_image: prepares the leaf image.
# detect_spots: identifies and counts visible disease spots.
# extract_color_features: extracts HSV color histograms from the image.
# load_model: loads a pre-trained classifier (from disk).
from preprocess import preprocess_image
from spot_detection import detect_spots
from features import extract_color_features
from train_classifier import load_model
import cv2

# Loads the trained Random Forest model from the model.pkl file
model = load_model("model.pkl")
# Specifies the path to the leaf image you want to analyze
img_path = "/media/ssd/leaf_images/sample_leaf.jpg"
# Calls your preprocess_image function: loads and resizes the image,
# converts it to HSV, applies Gaussian blur. Returns: image: the original,
# resized BGR image (used for features),blurred: blurred HSV version (used
# for spot detection)
image, blurred = preprocess_image(img_path)
# Uses the blurred HSV image to detect visible spots. Returns: spots:
# a list of dictionaries (with area, color, and shape of each spot); _: the
# mask image (you’re ignoring it here)
spots, _ = detect_spots(blurred)
# Uses the BGR image to extract HSV histogram features
features = extract_color_features(image)
# Passes the feature vector into the trained model.Returns a prediction:
# 0 = Healthy or 1 = Diseased
prediction = model.predict([features])[0]

print("Prediction:", "Diseased" if prediction else "Healthy")
print("Spots detected:", len(spots))
