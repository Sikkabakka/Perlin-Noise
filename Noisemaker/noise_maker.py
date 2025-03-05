import numpy as np
from random import uniform, randint
import os
import math



class Noise_maker():
    def __init__(self, grid_size, pixels):
        self.grid_size = grid_size
        self.pixels = pixels
        
        self.vectors = [ np.array([1, 1]), 
                        np.array([-1, 1]),
                        np.array([1, -1]),
                        np.array([-1, -1]),
                        np.array([np.sqrt(2), 0]),
                        np.array([0, np.sqrt(2)]),
                        np.array([-np.sqrt(2), 0]),
                        np.array([0, -np.sqrt(2)])
        ]
        self.grid_vectors = self.make_grid()

    def check_grid(self):
        for line in self.grid_vectors:
            for each in line:
                if sum(each**2) > 1:
                    print(sum(each**2))
                    print(each)
    def rand_vector(self):
        x = uniform(0, math.pi * 2)
        return np.array([np.cos(x), np.sin(x)])
        # index = randint(0, len(self.vectors)-1)
        # return self.vectors[index]
    
    def make_grid(self):
        return [[self.rand_vector() for j in range(self.grid_size +1)] for i in range(self.grid_size +1)]

    def find_corners(self, position):
        top_left = np.array([math.floor(position[0]), math.floor(position[1])]) 
        return [top_left, top_left + np.array([1, 0]), top_left + np.array([0, 1]), top_left + np.array([1, 1])]

    def lerp(self, x, y, t):
        return x + t*(y - x)
    
    def smoothstep(self, t):
        t = max(0, min(1, t))
        return t * t * (3 - 2 * t)
    def clamp(self, value):
        pass

    def find_value(self, position):
        corners = self.find_corners(position)

        corner_vectors = [position -corner for corner in corners] # riktig
        corner_normal_vectors = [self.grid_vectors[int(corner[0])][int(corner[1])] for corner in corners] #riktig

        dot_products = [np.dot(corner_normal_vectors[i], corner_vectors[i]) for i in range(4)]
       
      
        x_weight = self.smoothstep(position[0] - corners[0][0])
        l_interpolation = self.lerp(dot_products[0], dot_products[1], x_weight)
        s_interpolation = self.lerp(dot_products[2], dot_products[3], x_weight)

        y_weight = self.smoothstep(position[1]-corners[0][1])
        y_interpolation =self.lerp(l_interpolation, s_interpolation, y_weight)

        return y_interpolation
    def find_pixels(self, grid_index):
        
        map = []
        for i in range(self.pixels):
                temp = []
                for j in range(self.pixels):
                    # pixel = Pixel()
                    # pixel.pixel_count = (j, i)
                    # pixel.value = self.find_value(np.array([grid_index[0] + 1/self.pixels * j, grid_index[1]+ 1/self.pixels *i])) 
                    # pixel.position = grid_index[0] + 1/self.pixels * j, grid_index[1]+ 1/self.pixels *i
                    # pixel.corners = self.find_corners(pixel.position)
                    temp.append(self.find_value(np.array([grid_index[0] + 1/self.pixels * j, grid_index[1]+ 1/self.pixels *i])))
                map.append(temp)
        return map
    def make_map(self): 
        map = []
        for i in range(self.grid_size):
            temp = []
            for j in range(self.grid_size):
                temp.append(self.find_pixels((j, i)))
            map.append(temp)
            
        return map

if __name__ == "__main__":
    os.system("python3 main.py")