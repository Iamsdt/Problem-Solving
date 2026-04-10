import numpy as np


"""
Train a binary logistic regression classifier using gradient descent.
Implement the training loop and return the learned parameters (w, b).
"""


def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1 / (1 + np.exp(-z)), np.exp(z) / (1 + np.exp(z)))


def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # convert X and y to numpy arrays
    X = np.array(X)
    y = np.array(y)

    # initialize weights and bias
    w = np.zeros(X.shape[1])
    b = 0

    print(X, X.T)

    for _ in range(steps):
        # compute dot product
        z = np.dot(X, w) + b
        # compute predictions
        y_pred = _sigmoid(z)
        # apply gradient descent update
        dw = np.dot(X.T, (y_pred - y)) / len(y)
        db = np.sum(y_pred - y) / len(y)
        # binary cross-entropy loss gradient
        w -= lr * dw
        b -= lr * db

    return w, b


if __name__ == "__main__":
    X = [[0], [1], [2], [3]]
    y = [0, 0, 1, 1]
    lr = 0.1
    steps = 5000
    w, b = train_logistic_regression(X, y, lr, steps)
    print(f"w: {w}, b: {b}")
