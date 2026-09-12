# ============================================
# Project 2 - Data Classification Using AI
# DecodeLabs Internship
# ============================================

# Step 1: Import required libraries

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report


# Step 2: Load the Iris dataset

iris = load_iris()


# Step 3: Create a DataFrame to understand the dataset

data = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

data["target"] = iris.target


# Step 4: Display the dataset

print("========== IRIS DATASET ==========")
print(data.head())


# Step 5: Display information about the dataset

print("\n========== DATASET INFORMATION ==========")
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])
print("Features:", iris.feature_names)
print("Target classes:", iris.target_names)


# Step 6: Separate features (X) and target (y)

X = iris.data
y = iris.target


# Step 7: Split the dataset into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("\n========== DATA SPLIT ==========")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# Step 8: Create the classification model

model = KNeighborsClassifier(n_neighbors=3)


# Step 9: Train the model

model.fit(X_train, y_train)


# Step 10: Make predictions using the test data

y_pred = model.predict(X_test)


# Step 11: Calculate model accuracy

accuracy = accuracy_score(y_test, y_pred)

print("\n========== MODEL RESULTS ==========")
print("Model Accuracy:", round(accuracy * 100, 2), "%")


# Step 12: Display the classification report

print("\n========== CLASSIFICATION REPORT ==========")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))


# Step 13: Test the model with new data

new_flower = [[
    5.1,   # Sepal length
    3.5,   # Sepal width
    1.4,   # Petal length
    0.2    # Petal width
]]

prediction = model.predict(new_flower)

print("========== NEW FLOWER PREDICTION ==========")
print("Predicted flower:", iris.target_names[prediction[0]])