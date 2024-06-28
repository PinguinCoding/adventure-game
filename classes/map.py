import numpy as np


class Map(object):
    def __init__(self, name: str, shape: tuple):
        self.shape = shape
        self.matriz = np.full(shape, None)
        self.name = name
