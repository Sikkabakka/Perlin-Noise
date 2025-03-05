extends MeshInstance3D


var quality = 800
var layerer = Layerer.new(3, quality, 2)
var size = 800
func _ready() -> void:
	var arrays = []
	arrays.resize(Mesh.ARRAY_MAX)

	
	var map = layerer.make_layered_map()
	var vertices = PackedVector3Array()
	var amp =300
	
	var width = len(map[0])
	var height = len(map)

	var scale_factor = size / float(quality)
	for i in range(height):
		for j in range(width):
			vertices.append(Vector3(j * scale_factor, map[i][j] * scale_factor * amp, i * scale_factor))

			
	var indices = PackedInt32Array()
	for i in range(height-1):
		for j in range(width-1):
			var top_left = i*width+j
			var top_right = top_left +1
			var bottom_left = top_left + width
			var bottom_right = bottom_left +1
			
			indices.append(bottom_left)
			indices.append(top_left)
			indices.append(top_right)
			
			indices.append(bottom_left)
			indices.append(top_right)
			indices.append(bottom_right)
			
	print(len(map), len(map[0]))
	
	
	print(map[0][0], map[1][0])

	arrays[Mesh.ARRAY_VERTEX] = vertices
	
	arrays[Mesh.ARRAY_INDEX] = indices
	
	var st = SurfaceTool.new()
	st.create_from_arrays(arrays, Mesh.PRIMITIVE_TRIANGLES)
	st.generate_normals()
	mesh = st.commit()
	print("done")
	
	#Import alle pointsa fra python filen
	#lag en vertex liste
	#generer en indicies liste hvor du fokuserer på å lage trekanter mellom punkter
	#tegn
