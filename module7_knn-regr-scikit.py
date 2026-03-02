import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    N = int(input("Enter N (number of points): "))
    k = int(input("Enter k (number of neighbors): "))

    points = np.empty((N, 2), dtype=float)

    for i in range(N):
        x = float(input(f"Enter x for point {i + 1}: "))
        y = float(input(f"Enter y for point {i + 1}: "))
        points[i] = [x, y]

    X_train = points[:, 0].reshape(-1, 1)
    y_train = points[:, 1]

    X_query = float(input("Enter X to predict: "))

    if k > N:
        print(f"Error: k ({k}) is greater than N ({N}). Cannot perform k-NN regression.")
    else:
        model = KNeighborsRegressor(n_neighbors=k)
        model.fit(X_train, y_train)
        prediction = model.predict(np.array([[X_query]]))[0]
        print(f"Predicted Y: {prediction}")

    variance = np.var(y_train)
    print(f"Variance of labels in training dataset: {variance}")

if __name__ == "__main__":
    main()
