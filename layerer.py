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

        #må ikke bruke grid_size her!!!!!! 
        for i in range(grid_size):
            temp = []
            for x in range(pixels):
                for j in range(grid_size):
                        temp += layer[i][j][x] * amp
            fixed.append(temp)
        return fixed

    
    def normalize(data, min_val=0, max_val=1):
        min_data, max_data = np.min(data), np.max(data)
        return (data - min_data) / (max_data - min_data) * (max_val - min_val) + min_val


    def make_layered_map(self):
        
        layers = [self.make_noise(self.grid_size*2**i, self.size//(self.grid_size*2**i)) for i in range(self.layers)]
        print([len(layer) for layer in layers])
        layers = [self.fix_layer(layers[i], i) for i in range(len(layers))]
        print([len(layer) for layer in layers])

        added = []

        for i in range(self.size):
            temp = []
            for j in range(self.size):
                   print("hello")
                   print([len(layer) for layer in layers])
                   temp.append(self.normalize(sum([layer[i][j] for layer in layers])))
            added.append(temp)
        return added
if __name__ == "__main__":
    os.system("python3 main.py")
