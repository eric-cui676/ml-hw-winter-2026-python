import numpy as np
from sklearn.metrics import precision_score, recall_score

# Read number of points
N = int(input("Enter the number of points (N): "))

# Initialize arrays using NumPy
X = np.zeros(N, dtype=int)  # ground truth labels
Y = np.zeros(N, dtype=int)  # predicted labels

# Read N (x, y) points
for i in range(N):
    print(f"Point {i + 1}:")
    x = int(input("  Enter x (ground truth, 0 or 1): "))
    y = int(input("  Enter y (predicted, 0 or 1): "))
    X[i] = x
    Y[i] = y

# Compute Precision and Recall using Scikit-learn
precision = precision_score(X, Y, zero_division=0)
recall = recall_score(X, Y, zero_division=0)

print(f"\nPrecision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
