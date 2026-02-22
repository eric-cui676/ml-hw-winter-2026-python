import numpy as np


class KNNRegression:
    def __init__(self):
        self.points = None

    def fit(self, points):
        self.points = np.array(points, dtype=float)

    def predict(self, x, k):
        if k > len(self.points):
            raise ValueError(f"k={k} is greater than N={len(self.points)}")
        distances = np.abs(self.points[:, 0] - x)
        nearest_indices = np.argpartition(distances, k)[:k]
        return np.mean(self.points[nearest_indices, 1])


def main():
    n = int(input("Enter N (number of points): "))
    k = int(input("Enter k: "))

    points = []
    for i in range(n):
        print(f"Point {i + 1}:")
        x = float(input("  x = "))
        y = float(input("  y = "))
        points.append((x, y))

    model = KNNRegression()
    model.fit(points)

    x_query = float(input("Enter X for prediction: "))

    if k > n:
        print(f"Error: k ({k}) is greater than N ({n}).")
    else:
        result = model.predict(x_query, k)
        print(f"Predicted Y = {result}")


if __name__ == "__main__":
    main()
