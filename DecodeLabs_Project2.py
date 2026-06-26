import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ==========================================
# 1. INPUT PHASE (Raw Material & Loading)
# ==========================================
print("--- Phase 1: Loading Dataset ---")
# Load the classic Iris Benchmark dataset (150 balanced samples, 3 classes, 4 dimensions)
iris = load_iris()
X = iris.data  # Features: Sepal Length, Sepal Width, Petal Length, Petal Width
y = iris.target  # Targets: Setosa (0), Versicolor (1), Virginica (2)

print(f"Dataset successfully loaded.")
print(f"Features shape: {X.shape} (150 samples, 4 dimensions)")
print(f"Target classes: {iris.target_names}\n")

# ==========================================
# 2. PROCESS PHASE (The Engineering Pipeline)
# ==========================================
print("--- Phase 2: Processing & Training ---")

# Step A: Structural Integrity Split (Shuffle & Split into 80% Train / 20% Test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
print(f"Training set size: {X_train.shape[0]} samples")
print(f"Testing set size: {X_test.shape[0]} samples")

# Step B: Gatekeeper Rule (Feature Scaling using StandardScaler)
# This scales data so Mean = 0 and Variance = 1 to prevent bias in distance calculation
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Data scaling completed successfully.")

# Step C: Initialize and Train the KNN Algorithm
# K=3 is an ideal balance of simplicity and exceptionally high accuracy for Iris
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train_scaled, y_train)
print("KNN Model training completed.\n")

# ==========================================
# 3. OUTPUT PHASE (Validation & Metrics)
# ==========================================
print("--- Phase 3: Evaluation Metrics ---")

# Generate predictions on the test set
y_pred = knn_model.predict(X_test_scaled)

# Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"✨ Model Accuracy: {accuracy * 100:.2f}%")

# Generate the Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("\n📊 Confusion Matrix:")
print(conf_matrix)

# Generate detailed Classification Report (Includes F1-Score per class)
print("\n📝 Classification Report (F1-Score Metrics):")
print(classification_report(y_test, y_pred, target_names=iris.target_names))