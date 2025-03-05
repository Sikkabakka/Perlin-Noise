extends Sprite3D

var curve = Curve2D.new()

var heightmap = [1, 2, 5]
var spacing = 1
# Called when the node enters the scene tree for the first time.
func _ready() -> void:


	for x in range(heightmap.size()):
		var y = heightmap[x]  # Høydeverdien
		curve.add_point(Vector2(x * spacing, y))

	
	

	var smooth_points = curve.sample_baked(100)
	
	
	 # Flere punkter = glattere
	for point in smooth_points:
		print(point)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
