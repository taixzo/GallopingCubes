# GallopingCubes
 
Galloping Cubes is an algorithm for improving performance when using marching cubes to create geometry for CSG defined by signed distance fields. This repository contains a reference implementation of it in Python.

Speedups are significant with larger meshes:
| Grid size | Marching cubes | Galloping cubes |
| --------- | -------------- | --------------- |
| 10        | 0.20 sec       | 0.12 sec        |
| 20        | 1.63 sec       | 0.53 sec        |
| 40        | 12.46 sec      | 2.38 sec        |
| 80        | 1 min 38 sec   | 9.86 sec        |
| 160       | 13 min 1 sec   | 40.6 sec        |

This algorithm replaces the innermost loop in iterating through the cubes with raycasting. This allows each column to skip straight to the next cube that potentially intersects the surface defined by the SDF (hence "galloping"). Once at the surface, it steps forward one cube at a time until the distance to the surface (the absolute value of the SDF) is greater than the distance to the corner of the cube; at this point it casts another ray and repeats until it reaches the boundary.

For most shapes, this results in having to evaluate roughly 2n^2 cubes compared to n^3 for standard marching cubes. This results in immense speedups for high-resolution meshes. The worst possible case(a very densely detailed SDF that causes every cube to contain a boundary) would run about 1.2% slower than standard marching cubes; in every other situation galloping cubes will run significantly faster. It also parallelizes extremely well as every cube ray is still independent of the others, meaning this should allow high-resolution meshes to be generated in real-time on a GPU.
To use this library, call
```python
galloping_cubes.gallop_cubes(sdf, grid_size)
```

This returns a list of triangles. I've included a utility function `export_to_stl` which creates an ASCII STL string for visualization of the triangles generated.