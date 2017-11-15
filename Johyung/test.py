import pandas as pd
import tensorflow as tf
import numpy as np

def relu(x):
    return np.maximum(0,x)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#test code
class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std = 0.01):
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(input_size, output_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['b2'] = np.zeros(output_size)

team_stats = pd.read_csv("../Data/teams/team_stats")
results = pd.read_csv("../Data/results/game_results")

