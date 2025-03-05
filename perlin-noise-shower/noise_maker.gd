extends Node
class_name NoiseMaker

var grid_size: int
var pixels: int
var grid_vectors: Array

func _init(grid_size_: int, pixels_: int) -> void:
	grid_size = grid_size_
	pixels = pixels_
	grid_vectors = make_grid()

func rand_vector() -> Vector2:
	var x = randf() * PI * 2
	return Vector2(cos(x), sin(x))

func make_grid() -> Array:
	var grid = []
	for i in range(grid_size + 1):
		var row = []
		for j in range(grid_size + 1):
			row.append(rand_vector())
		grid.append(row)
	return grid

func find_corners(position: Vector2) -> Array:
	var top_left = Vector2(floor(position.x), floor(position.y))
	return [top_left, top_left + Vector2(1, 0), top_left + Vector2(0, 1), top_left + Vector2(1, 1)]

func lerp(x: float, y: float, t: float) -> float:
	return x + t * (y - x)

func smoothsatep(t: float) -> float:
	t = clamp(t, 0.0, 1.0)
	return t * t * (3.0 - 2.0 * t)

func find_value(position: Vector2) -> float:
	var corners = find_corners(position)
	var corner_vectors = []
	for corner in corners:
		corner_vectors.append(position - corner)
	
	var corner_normal_vectors = []
	for corner in corners:
		corner_normal_vectors.append(grid_vectors[int(corner.x)][int(corner.y)])
	
	var dot_products = []
	for i in range(4):
		dot_products.append(corner_normal_vectors[i].dot(corner_vectors[i]))
	
	var x_weight = smoothsatep(position.x- corners[0].x)
	var l_interpolation = lerp(dot_products[0], dot_products[1], x_weight)
	var s_interpolation = lerp(dot_products[2], dot_products[3], x_weight)
	
	var y_weight = smoothsatep(position.y - corners[0].y)
	return lerp(l_interpolation, s_interpolation, y_weight)

func find_pixels(grid_index: Vector2) -> Array:
	var map = []
	for i in range(pixels):
		var temp = []
		for j in range(pixels):
			var pos = Vector2(grid_index.x + 1.0 / pixels * j, grid_index.y + 1.0 / pixels * i)
			temp.append(find_value(pos))
		map.append(temp)
	return map

func make_map() -> Array:
	var map = []
	for i in range(grid_size):
		var temp = []
		for j in range(grid_size):
			temp.append(find_pixels(Vector2(j, i)))
		map.append(temp)
	return map
