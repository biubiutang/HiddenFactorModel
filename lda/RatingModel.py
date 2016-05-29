import numpy as np
from DataProcessor import DataLoader


class RatingModel:

    def __init__(self, ratings_filename='../Data/ratings.npz', n_hidden_factors=10):
        self.data = DataLoader.ratings_data(ratings_filename)
        n_users, n_items = self.data.shape

        self.alpha = 0.0
        self.beta_user = np.zeros(n_users)
        self.beta_item = np.zeros(n_items)
        self.gamma_user = np.zeros((n_users, n_hidden_factors))
        self.gamma_item = np.zeros((n_items, n_hidden_factors))