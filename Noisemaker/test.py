
grid_size = 10
i = 10

def map_to_range( x, in_min, in_max, out_min=0, out_max=1):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

print(map_to_range(1.1, -10, 1.2))