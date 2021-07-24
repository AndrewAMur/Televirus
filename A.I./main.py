# Library
from matplotlib import pyplot
import pandas as pd
import numpy as np

# Reading data
data = pd.read_csv()

# Turning data into numpy arrays
data = np.array(data)
m, n = data.shape
np.random.shuffle(data)

data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[:n]

data_train = data[100:m].T
Y_train = data_train[0]
X_train = data_train[1:n]

# Forward propagation
def init_params():
    W1 = np.random.rand(10, 784) - 0.5
    b1 = np.random.rand(10, 1) - 0.5
    W2 = np.random.rand(10, 10) - 0.5
    b2 = np.random.rand(10, 1) - 0.5
    return W1, W2, b1, b2

def ReLU():


def softmax():


def forward_prop():

# Back propagation
def one_hot():


def deriv_ReLU():


def back_prop():

# Updating parameters
def update_params():


def get_predictions():


def get_accuracy():


def gradient_descent():
    