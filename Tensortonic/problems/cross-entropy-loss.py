import numpy as np


def cross_entropy_loss(y_true, y_pred):
    # convert inputs to numpy arrays
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # number of samples
    m = y_true.shape[0]

    # select predicted probabilities for the correct classes
    correct_probs = y_pred[np.arange(m), y_true]

    # compute average negative log-probability
    loss = -np.mean(np.log(correct_probs))
    return loss


if __name__ == "__main__":
    # Input: y_true = [0, 1], y_pred = [[0.9, 0.1], [0.3, 0.7]]
    # Output: 0.231018
    y_true = [0, 1]
    y_pred = [[0.9, 0.1], [0.3, 0.7]]
    loss = cross_entropy_loss(y_true, y_pred)
    print(f"Loss: {loss}")
