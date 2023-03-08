from gallopingcubes import Vector3, march_cubes, gallop_cubes, export_to_stl

GRID_SIZE=20

def sdf(v):
	sphere = v.length() - GRID_SIZE
	sphere2 = (v+Vector3(2,0,0)).length() - GRID_SIZE
	return max(sphere, -sphere2)

triangles = march_cubes(sdf, GRID_SIZE)
stl = export_to_stl(triangles)

with open("out.stl", "w") as outfile:
    outfile.write(stl)