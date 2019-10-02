import numpy as np
import pandas as pd 

class Stats:
    
    # Class Attrubute
    species = 'math'

    # Initializer / Instance Attributes
    def __init__(self, data):
        self.data = list(data)

    # instance method
    def mean(self, scale=2):
        if scale != 2:
            return round(sum(self.data) / len(self.data), scale)
        else:
            return round(sum(self.data) / len(self.data), scale)

    # instance method
    def median(self):
        self.data.sort()
        if len(self.data) % 2 != 0:
            idx = int((len(self.data) - 1) / 2)
            return self.data[idx]
        else:
            idx_1 = self.data[int((len(self.data) / 2))]
            idx_2 = self.data[int((len(self.data) / 2) - 1)]
            return (idx_1 + idx_2) / 2

    # instance method
    def mode(self):
        self.data = list(self.data)
        counts = {}
        unique_nums = set(self.data)
        for digit in unique_nums:
            counts[digit] = self.data.count(digit)
        if max(counts.values()) == 1:
            print("No Mode exists")
        else:
            for key, value in counts.items():
                if value == max(counts.values()):
                    return key

    # instance method
    def variance(self, scale=2):
        self.data = np.array(self.data)
        if scale != 2:
            return round(((self.data - self.mean())**2).sum() / len(self.data), scale)
        else:
            return round(((self.data - self.mean())**2).sum() / len(self.data), scale)

    # instance method
    def standardDev(self, scale=2):
        if scale != 2:
            return round(self.variance()**(0.5), scale)
        else:
            return round(self.variance()**(0.5), scale)

    # instance method
    def coef_variation(self, scale=2):
        if scale != 2:
            return round((self.standardDev() / self.mean()), scale)
        else:
            return round((self.standardDev() / self.mean()), scale)
