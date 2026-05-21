import numpy as np

class Adaline:

    def __init__(self):
        self.lr = 0.01
        self.epochs = 10
        self.w = None
        self.b = 0

    def fit(self, X, y):

        self.w = np.zeros(X.shape[1])

        for i in range(self.epochs):

            y_pred = np.dot(X, self.w) + self.b

            error = y - y_pred

            self.w += self.lr * np.dot(X.T, error)
            self.b += self.lr * np.sum(error)

    def predict(self, X):
        return np.dot(X, self.w) + self.b


X = np.array([[1, 2],
              [2, 3],
              [3, 4]])

y = np.array([1, 1, 0])

a = Adaline()
a.fit(X, y)

print("Weights:", a.w)
print("Prediction:", a.predict([2, 3]))
