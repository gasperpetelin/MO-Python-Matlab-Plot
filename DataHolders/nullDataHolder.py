import numpy as np

class NullDataHolder:
    def __init__(self):
        self.df = None
        self.var = None
        self.obj = None

    def number_of_variables(self):
        return 2

    def number_of_objectives(self):
        return 0

    def filter(self, generation = None, front = None):
        return np.zeros((0, self.number_of_variables())), np.zeros((0, self.number_of_objectives()))

    def number_of_generations(self):
        return 10

    def number_of_fronts(self):
        return 10
