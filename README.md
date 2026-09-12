🤖 DecodeLabs Artificial Intelligence Internship Projects

This repository contains two Artificial Intelligence projects completed as part of the DecodeLabs Internship.

The projects demonstrate two important stages of learning Artificial Intelligence:

Project 1 — Rule-Based AI Chatbot

Project 2 — Data Classification Using Machine Learning

Together, these projects show the progression from manually programmed decision-making to a supervised machine learning model that learns patterns from data.

📌 Repository Overview

DecodeLabs-Internship-main/
│
├── README.md
│
├── project1/
│   ├── chatbot.py
│   └── readme.md
│
└── project2/
    ├── DataClassification.py
    └── readme.md

Projects at a glance

Project

Topic

Main Technology

Level

Project 1

Rule-Based AI Chatbot

Python

Beginner

Project 2

Data Classification

Python, Pandas, Scikit-learn, KNN

Beginner

🤖 Project 1 — Rule-Based AI Chatbot

📖 Description

Project 1 is a simple rule-based chatbot developed in Python.

Instead of using machine learning, the chatbot uses predefined rules and if-elif-else conditions to decide how to respond to the user's messages.

The chatbot accepts text input, checks it against known commands or phrases, and displays an appropriate response.

✨ Features

Responds to greetings such as hello, hi, and hey

Answers the question how are you

Identifies itself as a rule-based chatbot

Provides basic help

Responds to questions about having a good day

Responds when the user says they are doing well

Supports bye, exit, and quit commands

Continues running until the user exits

Cleans user input using .strip() and .lower()

🛠️ Technologies and Concepts

Python 3

if-elif-else statements

while loops

User input and output

String processing

Rule-based decision making

▶️ How to Run

Make sure Python 3 is installed:

python --version

Navigate to the Project 1 folder:

cd project1

Run the chatbot:

python chatbot.py

💬 Example

Chatbot: Hello! Type 'bye' to exit.
You: hello
Chatbot: Hello! How can I help you?

You: how are you
Chatbot: I'm doing well, thanks for asking!

You: what is your name
Chatbot: I'm a simple rule-based chatbot.

You: bye
Chatbot: Goodbye!

🎯 Learning Objectives

This project demonstrates:

Basic AI concepts

Conditional statements

Control flow

Loops

User input handling

String manipulation

Rule-based decision making

🌸 Project 2 — Data Classification Using AI

📖 Description

Project 2 is a basic supervised machine learning classification project built in Python.

The project uses the Iris dataset available through Scikit-learn and applies the K-Nearest Neighbors (KNN) algorithm to classify Iris flowers into their respective species.

The model learns from training data and then predicts the class of previously unseen data.

🌿 Iris Dataset

The Iris dataset contains measurements for three types of Iris flowers:

Iris Setosa

Iris Versicolor

Iris Virginica

The model uses four features:

Feature

Description

Sepal Length

Length of the sepal

Sepal Width

Width of the sepal

Petal Length

Length of the petal

Petal Width

Width of the petal

The target classes are:

0 → Setosa
1 → Versicolor
2 → Virginica

✨ Features

Loads the built-in Iris dataset

Creates a Pandas DataFrame

Displays sample dataset records

Displays dataset information

Shows the number of rows and columns

Displays feature names and target classes

Separates features and target values

Splits data into training and testing sets

Uses the K-Nearest Neighbors classification algorithm

Trains the machine learning model

Makes predictions on test data

Calculates model accuracy

Generates a classification report

Predicts the species of a new flower

🛠️ Technologies and Libraries

Python 3

Pandas — used for data handling and DataFrame creation

Scikit-learn — used for machine learning and evaluation

K-Nearest Neighbors (KNN) — classification algorithm

🧠 Machine Learning Workflow

The project follows a basic supervised learning pipeline:

Load Dataset
     ↓
Explore Data
     ↓
Separate Features and Target
     ↓
Split Training and Testing Data
     ↓
Create KNN Model
     ↓
Train Model
     ↓
Make Predictions
     ↓
Evaluate Accuracy
     ↓
Predict New Flower

Training and Testing Split

The dataset is divided into:

80% training data

20% testing data

A fixed random_state=42 is used so the split can be reproduced.

KNN Model

The project uses:

KNeighborsClassifier(n_neighbors=3)

The model uses the three nearest data points to help determine the predicted class.

▶️ How to Run

Check that Python is installed:

python --version

Navigate to the Project 2 folder:

cd project2

Install the required libraries:

pip install pandas scikit-learn

Run the program:

python DataClassification.py

🔮 New Flower Prediction

The program also tests the trained model using a new flower with these measurements:

Sepal Length: 5.1
Sepal Width: 3.5
Petal Length: 1.4
Petal Width: 0.2

The model then displays the predicted Iris species.

📊 Model Evaluation

The program evaluates the classifier using:

Accuracy

Accuracy represents the percentage of test samples classified correctly.

The output is displayed as:

Model Accuracy: XX.XX %

Classification Report

The classification report provides:

Precision

Recall

F1-score

Support

These metrics provide more detail about the model's performance for each flower class.

🎯 Learning Objectives

This project demonstrates:

Data handling

Dataset exploration

Feature and target separation

Training and testing data

Supervised learning

Classification

Model training

Prediction

Accuracy evaluation

Classification reports

Basic machine learning workflow

🔄 Comparison of the Two Projects

The two projects demonstrate different approaches to Artificial Intelligence.

Feature

Project 1

Project 2

AI Approach

Rule-based

Machine learning

Learning from Data

No

Yes

Main Concept

Predefined rules

Pattern learning

Algorithm

if-elif-else logic

KNN

Dataset Required

No

Iris dataset

Main Output

Chatbot responses

Flower classifications

Evaluation

User interaction

Accuracy and classification report

Main Difference

Project 1:
The developer explicitly defines the rules the chatbot follows.

Project 2:
The model learns patterns from existing data and uses those patterns to make predictions.

This makes the two projects a useful introduction to the difference between traditional rule-based systems and supervised machine learning.

🚀 Possible Future Improvements

Project 1 — Chatbot

The chatbot could be improved by:

Adding more conversation rules

Supporting more variations of user questions

Adding a larger vocabulary

Creating different chatbot personalities

Adding a graphical user interface

Connecting the chatbot to an external AI or NLP model

Project 2 — Data Classification

The classification project could be improved by:

Comparing KNN with other classification algorithms

Testing different values of n_neighbors

Visualizing the Iris dataset

Testing different train/test split ratios

Testing the model with additional flower measurements

Comparing the performance of multiple models

Adding a simple user interface for entering flower measurements

📚 What These Projects Demonstrate

By completing both projects, the repository demonstrates foundational knowledge of:

Python programming

Conditional logic

Loops

User input handling

Data processing

Pandas

Scikit-learn

Supervised machine learning

Classification

Model training

Model evaluation

Basic AI concepts

👩‍💻 Author

Laiba Noor

DecodeLabs Artificial Intelligence Internship

Projects included:

Artificial Intelligence Project 1 — Rule-Based AI Chatbot

Artificial Intelligence Project 2 — Data Classification Using AI

📄 Individual Project Documentation

For more detailed information about each project, see:

project1/readme.md

project2/readme.md
