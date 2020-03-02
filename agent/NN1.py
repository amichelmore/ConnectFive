import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
from lr_utils import load_dataset

def sigmoid(z):
    s = 1 / (1 + np.exp(-z))
    return s



class NeuralNet_one:

    def __init__(self, input, output, hidden, nodes):
        w = np.zeroes(shape=(input, 1))

        for i in range(hidden)
            w = np.append(w, w, 1)