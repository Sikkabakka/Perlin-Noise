extends Node

class_name Layerer

var layers: int
var size: int
var grid_size: int
var highest_value: float

func _init(layers_: int, size_: int, start_grid_size: int):
	layers = layers_
	size = size_
	grid_size = start_grid_size
	highest_value = 0.0
	for i in range(layers):
		highest_value += 1.0 / pow(2, i)

func make_noise(grid_size_: int, pixels: int):
	var noise_maker = NoiseMaker.new(grid_size_, pixels)
	return noise_maker.make_map()

func fix_layer(layer: Array, amp: float) -> Array:
	var fixed = []
	var grid_size_ = layer.size()
	var pixels = layer[0][0].size()
	var size_ = grid_size_ * pixels
	
	for i in range(size_):
		var row = int(i / (size_ / grid_size_))
		var row_row = i % pixels
		var temp = []
		for j in range(grid_size_):
			temp.append_array(layer[row][j][row_row])
		fixed.append(temp)
	
	return fixed

func map_to_range(x: float, in_min: float, in_max: float, out_min: float = 0.0, out_max: float = 1.0) -> float:
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

func make_layered_map() -> Array:
	var layers_ = []
	for i in range(layers):
		var grids = grid_size * pow(grid_size, i)
		var pixels = size / (grid_size * pow(grid_size, i))
		if (pixels * grids) < size:
			grids += int(ceil((size - pixels * grids) / pixels) + 1)
		layers_.append(make_noise(grids, pixels))
		print("Layer done" +str(i))

	for i in range(layers_.size()):
		layers_[i] = fix_layer(layers_[i], i)

	var added = []
	var highest_value_ = 0.0
	for i in range(size):
		var temp = []
		for j in range(size):
			var summen = 0.0
			for x in range(layers_.size()):
				var amp = 1.0 / pow(grid_size, x)
				summen += layers_[x][i][j] * amp
			if abs(summen) > highest_value_:
				highest_value_ = abs(summen)
			temp.append(summen)
		added.append(temp)

	for i in range(added.size()):
		for j in range(added[i].size()):
			added[i][j] = map_to_range(added[i][j], -highest_value_, highest_value_)

	return added
