from noise_maker import Noise_maker
import numpy as np
import os
import math 
class Layerer():
    def __init__(self, layers, size, start_grid_size):
        self.layers = layers
        self.size = size
        self.grid_size = start_grid_size

        self.highest_value = sum([1/2**(i) for i in range(self.layers)])
    def make_noise(self, grid_size, pixels):
        noise_maker = Noise_maker(grid_size, pixels)
        return noise_maker.make_map()
    
    def fix_layer(self, layer, amp):
        fixed = []

        grid_size = len(layer)
        pixels = len(layer[0][0])
        size = grid_size*pixels
        #må ikke bruke grid_size her!!!!!! 
        for i in range(size): #for hver row i fixed
            row = int(i//(size/grid_size)) #snapper den til rowen i griden
            row_row = i%pixels
            temp = []
            for j in range(grid_size):

                temp += layer[row][j][row_row] 

            fixed.append(temp)
        return fixed

    
    #må finne en funksjon som tar inn max og min value til 
    def map_to_range(self, x, in_min, in_max, out_min=0, out_max=1):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min



    def make_layered_map(self):
        layers = []
        for i in range(self.layers):
            grids = self.grid_size*self.grid_size**i
            pixels = self.size//(self.grid_size * self.grid_size**i)
            if (pixels * grids) < self.size:
                grids += int(math.ceil(self.size - pixels * grids) / pixels +1)

            
            layers.append(self.make_noise(grids, pixels))



        layers = [self.fix_layer(layers[i], i) for i in range(len(layers))]

        print([len(layer) for layer in layers])
        print([len(layer[0]) for layer in layers])
        print([(self.grid_size*2**i, self.size//(self.grid_size*2**i)) for i in range(self.layers)])
        added = []

        highest_value = 0
        for i in range(self.size):
            temp = []
            for j in range(self.size):
                summen = 0
                for x, layer in enumerate(layers):
                    amp = 1/self.grid_size**(x)
                    summen += layer[i][j] *amp
                
                if abs(summen) > highest_value:
                    highest_value = abs(summen)
                temp.append(summen)
                    
            added.append(temp)

        added = [[self.map_to_range(value, -highest_value, highest_value) for value in row] for row in added]

        return added
    
    #legg til amplitude
    #lag funksjon for å kalkulere highest value

    



if __name__ == "__main__":
    os.system("python3 main.py")
