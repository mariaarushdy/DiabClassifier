# DiabClassifier

DiabClassifier is a two-part project aimed at predicting the likelihood of an individual having diabetes and creating an intuitive web interface to interact with the model predictions.

## Overview

This repository contains the code for two essential components:

### 1. Machine Learning Model
File: `machine_learning_model.ipynb`

This Jupyter Notebook explores the following:

- Data loading and exploration from "diabetes_data.csv"
- Preprocessing and feature engineering
- Model selection and training using the K-Nearest Neighbors algorithm
- Model evaluation, hyperparameter tuning, and performance analysis

### 2. Streamlit Web Application
File: `streamlit_app.py`

This file contains the code for a Streamlit web application that allows users to interact with the trained model. Users can input relevant information, and the application will provide predictions regarding the likelihood of having diabetes.

## Machine Learning Model Details

The `machine_learning_model.ipynb` notebook details the steps for:

- Data preprocessing using pandas
- Model training with the K-Nearest Neighbors Classifier
- Model evaluation, performance assessment, and hyperparameter tuning using GridSearchCV
- Saving the trained model using pickle for later use

## Streamlit Web Application

The `streamlit_app.py` file constitutes the implementation of a user-friendly web interface using the Streamlit library. It allows individuals to interact with the machine learning model, input data, and receive predictions regarding their likelihood of having diabetes.

## Usage

1. To explore the machine learning model, open the `machine_learning_model.ipynb` Jupyter Notebook.
2. To run the Streamlit web application, execute the `streamlit_app.py` file.

## Dependencies

This project uses Python and several libraries like NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn, and Streamlit.

## Author

[Maria Roshdy]
