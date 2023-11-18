import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class Triangle:
    def __init__(self, p0, p1, p2):
        self.p0, self.p1, self.p2 = p0, p1, p2
        self.normal = np.cross(p1 - p0, p2 - p0)
        self.normal /= np.linalg.norm(self.normal)

    def intersect(self, ray_origin, ray_direction):
        denom = ray_direction.dot(self.normal)
        if abs(denom) < 1e-6:
            return None
        d = self.normal.dot(self.p0)
        t = -(ray_origin.dot(self.normal) + d) / denom
        if t < 0:
            return None
        m = ray_origin + ray_direction * t
        u = self.p1 - self.p0
        v = self.p2 - self.p0
        w = m - self.p0
        vCrossW = np.cross(v, w)
        vCrossU = np.cross(v, u)
        if vCrossW.dot(vCrossU) < 0:
            return None
        uCrossW = np.cross(u, w)
        uCrossV = np.cross(u, v)
        if uCrossW.dot(uCrossV) < 0:
            return None
        denom = np.linalg.norm(uCrossV)
        r = np.linalg.norm(vCrossW) / denom
        t = np.linalg.norm(uCrossW) / denom
        return r <= 1 and t <= 1 and r + t <= 1

# Define a pyramid as four triangles
pyramid = [
    Triangle(np.array([0., 0., 0.]), np.array([1., 0., 0.]), np.array([0.5, 1., 0.5])),
    Triangle(np.array([0., 0., 0.]), np.array([0., 1., 0.]), np.array([0.5, 1., 0.5])),
    Triangle(np.array([1., 0., 0.]), np.array([1., 1., 0.]), np.array([0.5, 1., 0.5])),
    Triangle(np.array([0., 1., 0.]), np.array([1., 1., 0.]), np.array([0.5, 1., 0.5]))
]

# Define the ray
ray_origin = np.array([-1., -1., -1.])
ray_direction = np.array([1., 1., 1.])
ray_direction /= np.linalg.norm(ray_direction)

# Check for intersection with each triangle of the pyramid
for i, triangle in enumerate(pyramid):
    if triangle.intersect(ray_origin, ray_direction):
        print(f"The ray intersects triangle {i} of the pyramid.")

# Visualize the pyramid and the ray using matplotlib

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the pyramid
x = [triangle.p0[0] for triangle in pyramid]
y = [triangle.p0[1] for triangle in pyramid]
z = [triangle.p0[2] for triangle in pyramid]
vertices = [list(zip(x,y,z))]
ax.add_collection3d(Poly3DCollection(vertices))

# Plot the ray
t = np.linspace(-2,2,400)
x,y,z = [ray_origin[i] + t*ray_direction[i] for i in range(3)]
ax.plot(x,y,z,label='ray')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
