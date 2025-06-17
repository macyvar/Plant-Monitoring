"""
@file train_classifier.py

@brief This module handles the training and loading of a machine learning model
    for classifying plant leaf health. It uses a Random Forest classifier
    trained on color histogram features extracted from leaf images.

@functions
- train_model(data_folder): Trains a RandomForest model on labeled images and saves it.
- load_model(path): Loads a previously saved model from disk.

@dependencies
- scikit-learn
- OpenCV (cv2)
- joblib
- features.py for feature extraction
@author
    Macy Varga
"""

## Imports
# For file and folder handling (paths, listing files)
import os
# OpenCV – used for reading and processing images
import cv2
# Handles numerical arrays (features)
import numpy as np
# RandomForestClassifier: Your machine learning model
# from scikit-learn
from sklearn.ensemble import RandomForestClassifier
# train_test_split: Splits your dataset into training
# and testing sets
from sklearn.model_selection import train_test_split
# joblib: Saves and loads the trained model
import joblib
# extract_color_features: Your custom function (from
# features.py) to get feature vectors from leaf images
from features import extract_color_features

## Model Loader
# Loads a previously trained model from a .pkl file
# using joblib. Running predictions later using
# main.py without re-training
def load_model(path):
    return joblib.load(path)

## Model Trainer
# X will store the feature vectors extracted from the
# images. y will store the corresponding labels: 0 for
# healthy, 1 for diseased
def train_model(data_folder):
    X = []
    y = []

    # Loops through 2 categories: label = 0 for "healthy", label =
    # 1 for "diseased". Builds a path like data_folder/healthy or
    # data_folder/diseased
    for label, class_name in enumerate(["healthy", "diseased"]):
        class_path = os.path.join(data_folder, class_name)

        # Lists all image files in the class folder, builds full file
        # path, and loads the image using OpenCV (cv2.imread())
        for file in os.listdir(class_path):
            file_path = os.path.join(class_path, file)
            image = cv2.imread(file_path)

            #Ensures the image loaded correctly, extracts color
            # histogram features using your custom function,
            # appends the feature vector to X and the label (0 or 1) to y
            if image is not None:
                features = extract_color_features(image)
                X.append(features)
                y.append(label)

    # Splits the dataset into 80% training, 20% testing.
    # random_state=42 ensures reproducibility.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Initializes a Random Forest with 100 trees, trains it using your extracted features
    # and labels
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)

    # Evaluates accuracy on the test set. Saves the trained model to a
    # file (model.pkl) for future use.
    print("Test accuracy:", clf.score(X_test, y_test))
    joblib.dump(clf, "model.pkl")