# Human Activity Recognition Using Machine Learning

## 1. Project Overview

Human Activity Recognition (HAR) is a machine learning project that identifies human physical activities using sensor data.

This project uses a pre-collected smartphone sensor dataset containing accelerometer and gyroscope readings. These readings are processed and used to train a machine learning model that classifies different human activities.

The main goal is to understand how sensor data can be explored, processed, and used to build an activity classification model.

**Note:** This project uses an existing dataset for model training and prediction. It does not collect live sensor readings from a smartphone.

## 2. Project Objectives

- Understand accelerometer and gyroscope sensor data.
- Explore and analyze the dataset.
- Process sensor readings and activity labels.
- Extract meaningful statistical features.
- Train a machine learning classification model.
- Evaluate model performance.
- Predict human activities using the trained model.

## 3. Dataset Description

This project uses the **Smartphone-Based Recognition of Human Activities and Postural Transitions** dataset from the UCI Machine Learning Repository.

The dataset contains:
- Accelerometer readings.
- Gyroscope readings.
- Activity labels.
- Experiment and participant information.
- Start and end positions of activity segments.

### Activity Classes

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

## 4. Dataset Download and Setup

The original dataset is not included in this GitHub repository.

Download it from the official UCI Machine Learning Repository:

**Dataset:** Smartphone-Based Recognition of Human Activities and Postural Transitions

**Download:** https://archive.ics.uci.edu/dataset/341/smartphone+based+recognition+of+human+activities+and+postural+transitions

### Dataset Setup

1. Download the dataset from the UCI website.
2. Extract the downloaded ZIP file.
3. Place the extracted dataset inside the project's `dataset/raw/` directory.
4. Ensure the extracted folder structure matches the paths used in the Jupyter Notebook.

The dataset includes folders and files such as `RawData`, `Train`, `Test`, `activity_labels.txt`, `features.txt`, and `README.txt`.

**Dataset Citation:**

Reyes-Ortiz, J., Anguita, D., Oneto, L., and Parra, X. (2015). Smartphone-Based Recognition of Human Activities and Postural Transitions. UCI Machine Learning Repository.

DOI: 10.24432/C54G7M

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0).

## 5. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

## 6. Project Workflow

1. **Dataset Loading:** Load the pre-collected accelerometer, gyroscope, and activity label files.
2. **Data Exploration:** Understand the dataset structure, sensor readings, and activity distribution.
3. **Data Validation:** Check recording matches, activity labels, and segment boundaries.
4. **Activity Segmentation:** Extract sensor readings corresponding to each labeled activity.
5. **Feature Extraction:** Calculate statistical features such as mean, standard deviation, minimum, maximum, and energy.
6. **Model Training:** Train a Random Forest Classifier using the extracted features.
7. **Model Evaluation:** Evaluate the model using test data and classification metrics.
8. **Activity Prediction:** Use the saved model to predict activities from sample feature inputs.

## 7. Machine Learning Model

The project uses a **Random Forest Classifier** for human activity classification.

The initial model achieved **96.30% accuracy** using a random 80:20 train-test split.

This is a preliminary result. Further evaluation is required using an improved validation approach before treating it as the final model performance.

## 8. Project Structure

```text
human-activity-recognition1/
│
├── dataset/
│   └── raw/
│
├── models/
│   ├── random_forest_model.pkl
│   ├── scaler.pkl
│   └── sample_input.csv
│
├── notebooks/
│   └── 01_Data_Exploration.ipynb
│
├── src/
│   └── predict.py
│
├── visualizations/
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 9. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/nehamanjunath2006-bit/human-activity-recognition1.git
```

### Step 2: Navigate to the Project Folder

```bash
cd human-activity-recognition1
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### Step 5: Install Required Libraries

The project includes a `requirements.txt` file containing the required Python libraries.

Install them using:

```bash
pip install -r requirements.txt
```

### Step 6: Download and Set Up the Dataset

Follow the instructions in the Dataset Download and Setup section.

## 10. Running the Project

### Model Exploration and Training

Open the following Jupyter Notebook:

```text
notebooks/01_Data_Exploration.ipynb
```

Run the notebook cells to explore the dataset, extract features, train the model, and evaluate its performance.

### Activity Prediction

Run the prediction script:

```bash
python src/predict.py
```

The script loads the saved Random Forest model, scaler, and sample input to predict a human activity.

**Example Output:**

```text
Predicted Human Activity: SITTING
```

The prediction is based on sample feature input, not live smartphone sensor readings.

## 11. Current Implementation Status

- Dataset exploration and validation – Completed
- Accelerometer and gyroscope data loading – Completed
- Activity segmentation – Completed
- Statistical feature extraction – Completed
- Data visualization – Completed
- Initial Random Forest model training – Completed
- Model and scaler saving – Completed
- Standalone prediction script – Implemented
- Improved model evaluation – Pending

## 12. Future Enhancements

- Improve model evaluation and generalization.
- Experiment with additional machine learning algorithms.
- Develop a simple interface for activity prediction.
- Explore real-time smartphone sensor integration as a future enhancement.

## 13. Conclusion

This project demonstrates how machine learning can be applied to pre-collected smartphone sensor data to recognize human physical activities.

It provides practical experience in dataset exploration, sensor data processing, feature extraction, machine learning model development, evaluation, and prediction.