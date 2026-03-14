import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# --- Read Training Set ---
N = int(input("Enter the number of training samples (N): "))

train_X = np.empty(N, dtype=float)
train_Y = np.empty(N, dtype=int)

print(f"Enter {N} (x, y) pairs for the training set:")
for i in range(N):
    train_X[i] = float(input(f"  Pair {i + 1} - x: "))
    train_Y[i] = int(input(f"  Pair {i + 1} - y: "))

# --- Read Test Set ---
M = int(input("Enter the number of test samples (M): "))

test_X = np.empty(M, dtype=float)
test_Y = np.empty(M, dtype=int)

print(f"Enter {M} (x, y) pairs for the test set:")
for i in range(M):
    test_X[i] = float(input(f"  Pair {i + 1} - x: "))
    test_Y[i] = int(input(f"  Pair {i + 1} - y: "))

# Reshape X arrays to 2D as required by scikit-learn (n_samples, n_features)
train_X_2d = train_X.reshape(-1, 1)
test_X_2d = test_X.reshape(-1, 1)

# --- Find the best k in range [1, 10] ---
best_k = 1
best_accuracy = 0.0

for k in range(1, 11):
    if k > N:
        break  # k cannot exceed the number of training samples
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_X_2d, train_Y)
    predictions = knn.predict(test_X_2d)
    accuracy = accuracy_score(test_Y, predictions)
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_k = k

print(f"\nBest k: {best_k}")
print(f"Test Accuracy: {best_accuracy:.4f}")
