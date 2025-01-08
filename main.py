import numpy as np
from random import uniform

import math

class Noise_maker():
    def __init__(self, size):
        self.size = size
        self.grid = self.make_grid(self.size)

    def rand_vector(self):
        x = uniform(0, math.pi * 2)
        return np.array([np.cos(x), np.sin(x)])
    
    def make_grid(self, size):
        return [[self.rand_vector() for i in range(size)] for i in range(size)]
    def find_value(self, position):
        #ta en position, finn alle vectorene i hjørnene, også finne noe annet også
        #noe med dot product, men dette skal være lett
        pass
    def find_corners(self, index):
        pass

noise_maker = Noise_maker(3)
print(noise_maker.grid)