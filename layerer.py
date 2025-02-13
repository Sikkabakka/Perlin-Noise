from noise_maker import Noise_maker
import numpy as np
import os
class Layerer():
    def __init__(self, layers, size, start_grid_size, start_amplitude):
        self.layers = layers
        self.size = size
        self.grid_size = start_grid_size
        self.amplitude = start_amplitude

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
    def map_to_range(x, in_min, in_max, out_min=0, out_max=1):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min



    def make_layered_map(self):
        
        layers = [self.make_noise(self.grid_size*2**i, self.size//(self.grid_size*2**i)) for i in range(self.layers)]

        layers = [self.fix_layer(layers[i], i) for i in range(len(layers))]


        added = []

        for i in range(self.size):
            temp = []
            for j in range(self.size):
                   print([layer[i][j] for layer in layers])
                   print(sum([layer[i][j] for layer in layers]))
                   temp.append(self.normalize(sum([layer[i][j] for layer in layers])))
            added.append(temp)
        return added
if __name__ == "__main__":
    os.system("python3 main.py")
