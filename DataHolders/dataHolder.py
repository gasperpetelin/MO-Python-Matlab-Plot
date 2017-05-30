import numpy as np

class DataHolder:
    def __init__(self, df, gen, itr, fr, var, obj):
        self.df = df
        self.gen = gen
        self.itr = itr
        self.fr = fr
        self.var = var
        self.obj = obj

    def number_of_variables(self):
        return len(self.var)

    def number_of_objectives(self):
        return len(self.obj)

    def filter(self, generation = None, front = None):
        df = self.df
        if(generation != None):
            sel = df[:, self.gen] == generation
            df = df[sel,:]
        if(front != None):
            sel = df[:, self.fr] == front
            df = df[sel,:]
        return df[:, self.var], df[:, self.obj]

    def number_of_generations(self):
        return int(np.max(self.df[:, self.gen]))

    def number_of_fronts(self):
        return int(np.max(self.df[:, self.fr]))

    def get_objective_limits(self, objective):
        objectives_df = self.df[:, self.obj]
        objective_column = objectives_df[:, objective]
        return [np.min(objective_column), np.max(objective_column)]

