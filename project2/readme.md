# 🌸 Data Classification Using AI

A basic **machine learning classification project** built in Python as part of **Artificial Intelligence Project 2** at DecodeLabs.

This project uses the **Iris dataset** and a **K-Nearest Neighbors (KNN)** classification algorithm to train a model that can identify different types of Iris flowers based on their physical measurements.

The project demonstrates the basic **supervised learning pipeline**, including loading data, understanding the dataset, splitting data into training and testing sets, training a model, evaluating its performance, and making predictions on new data.

## 📌 Project Overview

The goal of this project is to build a basic classification model using a small dataset.

The Iris dataset contains measurements of flowers that belong to three different classes:

* 🌱 Iris Setosa
* 🌸 Iris Versicolor
* 🌺 Iris Virginica

The model learns patterns from the training data and uses those patterns to classify previously unseen test data and a new flower sample.

This project represents the transition from simple rule-based logic to **supervised machine learning**, where the model learns from existing data rather than relying entirely on manually written rules.

## ✨ Features

* 📊 Loads the built-in Iris dataset
* 🔍 Displays the first few rows of the dataset
* 📋 Displays dataset information
* 📈 Shows the number of rows and columns
* 🌿 Displays the available features and target classes
* ✂️ Splits the dataset into training and testing sets
* 🤖 Uses the K-Nearest Neighbors (KNN) algorithm
* 🧠 Trains the classification model
* 🔮 Makes predictions on test data
* 📊 Calculates model accuracy
* 📑 Generates a classification report
* 🌸 Tests the trained model with a new flower sample

## 🛠️ Technologies Used

* **Python 3**
* **Pandas** — for creating and displaying the dataset in a DataFrame
* **Scikit-learn** — for dataset loading, train/test splitting, machine learning, and evaluation
* **K-Nearest Neighbors (KNN)** — classification algorithm

## 📂 Dataset

This project uses the **Iris dataset**, which is available directly through Scikit-learn.

The dataset contains four flower measurements:

| Feature      | Description         |
| ------------ | ------------------- |
| Sepal Length | Length of the sepal |
| Sepal Width  | Width of the sepal  |
| Petal Length | Length of the petal |
| Petal Width  | Width of the petal  |

The target variable represents the flower species.

The three target classes are:

```text
0 → Setosa
1 → Versicolor
2 → Virginica
```

## 🧠 Machine Learning Workflow

The project follows these main steps:

### 1. Import Libraries

The required Python libraries are imported:

```python
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
```

### 2. Load the Dataset

The Iris dataset is loaded using Scikit-learn:

```python
iris = load_iris()
```

### 3. Understand the Data

A Pandas DataFrame is created to display the dataset and its target values.

The program also displays:

* Number of rows
* Number of columns
* Feature names
* Target class names

### 4. Separate Features and Target

The input features are stored in `X`, while the target classes are stored in `y`.

```python
X = iris.data
y = iris.target
```

### 5. Split the Dataset

The dataset is divided into:

* **80% training data**
* **20% testing data**

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The training data is used to teach the model, while the testing data is used to evaluate how well the trained model performs on unseen data.

### 6. Create the KNN Model

A K-Nearest Neighbors classifier is created with `3` neighbors:

```python
model = KNeighborsClassifier(n_neighbors=3)
```

### 7. Train the Model

The model learns from the training data:

```python
model.fit(X_train, y_train)
```

### 8. Make Predictions

The trained model predicts the classes of the test samples:

```python
y_pred = model.predict(X_test)
```

### 9. Evaluate the Model

The model's accuracy is calculated using:

```python
accuracy_score(y_test, y_pred)
```

A detailed classification report is also displayed.

### 10. Predict a New Flower

Finally, the trained model is given a new flower's measurements:

```text
Sepal Length: 5.1
Sepal Width: 3.5
Petal Length: 1.4
Petal Width: 0.2
```

The model predicts which Iris species the flower belongs to.

## 📊 Model Evaluation

The project evaluates the model using:

### Accuracy

Accuracy shows the percentage of test predictions that were classified correctly.

The program displays the result in this format:

```text
Model Accuracy: XX.XX %
```

### Classification Report

The classification report provides additional evaluation metrics for each class, including:

* Precision
* Recall
* F1-score
* Support

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed.

Check your Python version:

```bash
python --version
```

### 2. Install Required Libraries

Install Pandas and Scikit-learn:

```bash
pip install pandas scikit-learn
```

### 3. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 4. Open the Project Folder

```bash
cd data-classification-ai
```

### 5. Run the Program

If your Python file is named `classification.py`:

```bash
python classification.py
```

## 📂 Project Structure

```text
data-classification-ai/
│
├── classification.py
└── README.md
```

### Files

**`classification.py`**

Contains the complete machine learning implementation, including:

* Dataset loading
* Data exploration
* Data splitting
* KNN model creation
* Model training
* Prediction
* Accuracy evaluation
* Classification report
* New flower prediction

**`README.md`**

Contains the documentation and instructions for the project.

## 🎯 Learning Objectives

This project demonstrates the following fundamental AI and machine learning concepts:

* Data handling
* Dataset exploration
* Feature and target separation
* Training and testing data
* Supervised learning
* Classification
* Model training
* Model prediction
* Accuracy evaluation
* Classification reports
* Using machine learning to recognize patterns in data

These concepts directly align with the Project 2 objective of building a basic classification model and learning the fundamentals of supervised learning.

## 🚀 Possible Improvements

The project can be extended by:

* Comparing KNN with other classification algorithms
* Testing different values of `n_neighbors`
* Testing the model with additional new flower measurements
* Visualizing the Iris dataset
* Comparing different train/test split ratios
* Experimenting with model performance and accuracy

The project material specifically encourages experimenting with different algorithms and testing the model with completely new data.

## 👩‍💻 Author

**Laiba Noor**

Artificial Intelligence — Project 2
**Data Classification Using AI**

---

### 📚 Project

This project was completed as part of the **DecodeLabs Artificial Intelligence Internship — Project 2**.

The project focuses on building a foundation in **supervised learning, data handling, and model training**.
