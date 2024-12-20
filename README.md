# Zoho Assessment Project

# Audience Rating Prediction Using Machine Learning Pipelines
This project focuses on building a machine learning model to predict audience ratings for movies using the Rotten Tomatoes dataset. It demonstrates the application of pipelines for efficient preprocessing, model training, and evaluation. The project also integrates hyperparameter tuning for optimal model performance and evaluates the model's predictions against real data.

# Table of Contents
Overview
Dataset
Features and Preprocessing
Pipeline Design
Hyperparameter Tuning
Evaluation Metrics
Results and Visualizations
Installation and Usage
Contributing
License

# Overview
The objective of this project is to predict audience ratings for movies using machine learning techniques. The pipeline structure ensures smooth preprocessing and integration of various tasks such as scaling, label encoding, and model training.

# Dataset
The dataset used for this project is derived from Rotten Tomatoes. It consists of 16,650 rows and multiple features describing movies, such as:

Movie-specific attributes
Ratings and reviews
Release dates

# Key Target:
audience_rating: This is the column predicted by the model.

# Features and Preprocessing
The dataset underwent the following preprocessing steps:

Datetime Features:
Extracted year, month, and day from date columns.
Dropped original datetime columns post-transformation.
Categorical Features:
Label encoding was applied to convert categorical data into numerical form.
Missing Values:
Rows with missing data were removed for a clean dataset.
Class Imbalance:
Applied SMOTE (Synthetic Minority Oversampling Technique) to balance the target classes.

# Pipeline Design
The pipeline automates the following steps:

Standard Scaling: Normalizes numerical features for uniformity.
Random Forest Classifier: A robust machine learning model for predictions.

# Hyperparameter Tuning
The project uses GridSearchCV to tune hyperparameters, optimizing:

Number of estimators
Maximum depth of the trees
Minimum samples split
This ensures the best model parameters for accurate predictions.

# Evaluation Metrics
The model is validated using:

# Confusion Matrix
Classification Report
Accuracy, Precision, Recall, and F1-Score
Additionally, the pipeline predicts audience ratings on the test set, and results are visualized for better understanding.

# Results and Visualizations
Key results:

High accuracy and balanced performance across classes.
Clear visualization of the confusion matrix and actual vs. predicted ratings.
Example plots included:

Confusion Matrix Heatmap.
Actual vs Predicted Ratings Scatter Plot.

# Installation and Usage
Prerequisites
Python 3.8+
Required Python libraries:
pandas
numpy
scikit-learn
matplotlib
seaborn
imbalanced-learn
joblib

# Contributing
Contributions are welcome! If you'd like to improve this project, please fork the repository and submit a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Contact
For questions or feedback, reach out via email at karthickr608@gmail.com.

