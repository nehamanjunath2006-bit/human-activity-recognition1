# Human Activity Recognition Using Machine Learning

## 1. Project Overview

Human Activity Recognition (HAR) is a machine learning project that identifies human physical activities using sensor data.

This project uses an existing, pre-collected smartphone sensor dataset containing accelerometer and gyroscope readings. A machine learning model is trained on these readings to recognize different human activities.

The main objective is to understand how sensor data can be processed, analyzed, and used to build an activity classification model.

**Note:** This project uses an existing dataset for model training and prediction. It does not collect live sensor readings from a smartphone.

## 2. Project Objectives

- Understand smartphone accelerometer and gyroscope data.
- Explore and analyze the available dataset.
- Process sensor readings and activity labels.
- Extract meaningful statistical features.
- Train a machine learning classification model.
- Evaluate model performance.
- Predict activities using the trained model.

## 3. Dataset Description

The project uses the Smartphone-Based Recognition of Human Activities and Postural Transitions dataset.

The dataset contains:
- Accelerometer readings.
- Gyroscope readings.
- Activity labels.
- Experiment and participant information.
- Start and end positions for activity segments.

The dataset contains 12 activity classes:

1. Walking
2. Walking Upstairs
3. Walking Downstairs
4. Sitting
5. Standing
6. Laying
7. Stand to Sit
8. Sit to Stand
9. Sit to Lie
10. Lie to Sit
11. Stand to Lie
12. Lie to Stand

## 4. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

## 5. Project Workflow

1. **Dataset Loading:** Load the pre-collected accelerometer, gyroscope, and activity label files.
2. **Data Exploration:** Understand the dataset structure, sensor readings, and activity distribution.
3. **Data Validation:** Check recording matches, activity labels, and segment boundaries.
4. **Segmentation:** Extract sensor readings corresponding to each labeled activity.
5. **Feature Extraction:** Calculate statistical features such as mean, standard deviation, minimum, maximum, and energy.
6. **Model Training:** Train a Random Forest Classifier using the extracted features.
7. **Model Evaluation:** Evaluate the trained model using test data and classification metrics.
8. **Prediction:** Use the saved model to predict activities from sample feature inputs.

## 6. Machine Learning Model

The project uses a Random Forest Classifier for activity classification.

The initial model achieved **96.30% accuracy** using a random 80:20