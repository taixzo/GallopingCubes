import time
from gallopingcubes import Vector3, march_cubes, gallop_cubes, export_to_stl

GRID_SIZE=160

def sdf(v):
	sphere = v.length() - GRID_SIZE
	sphere2 = (v+Vector3(GRID_SIZE/2,0,0)).length() - GRID_SIZE
	return max(sphere, -sphere2)

# start = time.time()
# marched_triangles = march_cubes(sdf, GRID_SIZE)
# end = time.time()
# print("Time taken for marching cubes: ", end - start)

start = time.time()
galloped_triangles = gallop_cubes(sdf, GRID_SIZE)
end = time.time()
print("Time taken for galloping cubes: ", end - start)


# marched_stl = export_to_stl(galloped_triangles)
# galloped_stl = export_to_stl(galloped_triangles)

# print("Writing files...", end="")
# with open("marched.stl", "w") as outfile:
#     outfile.write(marched_stl)
# with open("galloped.stl", "w") as outfile:
#     outfile.write(galloped_stl)
# print ("Done!")