import numpy as np

from DataHolders.dataHolder import DataHolder


class FileParser():
    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self):
        file = np.genfromtxt(self.file_name, dtype=float, delimiter=',', comments="#")

        with open(self.file_name, "r") as fi:
            for ln in fi:
                if ln.startswith("#"):
                    break

        ln = ln.replace("#","",1).strip().split(",")
        generation = 0
        subject = 1
        front = 2
        variables = [x+3 for x in range(int(ln[0]))]
        objectives = [x+3+len(variables) for x in range(int(ln[1]))]
        return DataHolder(file, generation, subject, front, variables, objectives)

