import numpy as np
from random import uniform, randint
import os
import math


class Noise_maker():
    def __init__(self, grid_size, pixels):
        self.grid_size = grid_size
        self.pixels = pixels
        self.grid_vectors = self.make_grid(self.grid_size)

    def rand_vector(self):
        x = uniform(0, math.pi * 2)
        return np.array([np.cos(x), np.sin(x)])
    
    def make_grid(self, size):
        return [[self.rand_vector() for i in range(size)] for i in range(size)]

    def find_corners(self, position):
        top_left = np.array([math.floor(position[0]), math.floor(position[1])])
        return [top_left, top_left + np.array([1, 0]), top_left + np.array([0, 1]), top_left + np.array([1, 1])]

    def cubic_interpolation(self, first_position, second_position, weight):
        return (second_position - first_position)* (3.0-weight*2)*weight**2 + first_position
    
    def weight_calc(self, t):
        return 6 * t**5 - 15 * t**4 + 10 * t**3

    def find_value(self, position):
        corners = self.find_corners(position)

        corner_vectors = [position -corner for corner in corners]
        corner_normal_vectors = [self.grid_vectors[corner[0]][corner[1]] for corner in corners]

        dot_products = [np.dot(corner_normal_vectors[i], corner_vectors[i]) for i in range(4)]
        weights = self.weight_calc(position - corners[0])


        first_interpolation = self.cubic_interpolation(dot_products[0], dot_products[2], weights[0])
        second_interpolation = self.cubic_interpolation(dot_products[1], dot_products[3], weights[0])

        third_interpolation = self.cubic_interpolation(first_interpolation, second_interpolation, weights[1])
        return third_interpolation
    def make_map(self):
        value = 0
        map = []
        for i in range(self.pixels-1):
            temp = []
            for j in range(self.pixels-1):
                value = self.find_value(np.array([self.grid_size/(self.pixels -i), self.grid_size/(self.pixels -j)])) 
                temp.append(value)
            map.append(temp)
        return map