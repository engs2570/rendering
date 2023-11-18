# Sure, here’s a simple example of a path tracer in Python.
# This is a very basic implementation and real-world path tracers would be much more complex and optimized.
# This example only traces a single ray per pixel and does not handle materials, shadows, or indirect light.

import numpy as np
import matplotlib.pyplot as plt

# Here we’re setting up the scene. We define the dimensions of the image we’re going to render (WIDTH and HEIGHT),
# the position of the camera in 3D space (camera_pos), and the position and radius of a sphere that we’re going to render.


# Scene setup
WIDTH, HEIGHT = 640, 480
camera_pos = np.array([0, 0, 0])
sphere_center = np.array([0, 0, -5])
sphere_radius = 1

# Create an image
image = np.zeros((HEIGHT, WIDTH, 3))


# For each pixel
for y in range(HEIGHT):
    for x in range(WIDTH):

        # # These lines start a loop over each pixel in the image. For each pixel, we’re going to compute a color based on whether the pixel’s corresponding ray hits the sphere.

        # Compute the viewing ray
        ray_dir = np.array([x - WIDTH / 2, y - HEIGHT / 2, -WIDTH]) / WIDTH
        ray_dir /= np.linalg.norm(ray_dir)  # Normalize

        # Here we’re computing the direction of the viewing ray for the current pixel. The viewing rays are assumed to originate from the camera position and pass through each pixel of an imaginary image plane located at z = -1.

        # Compute the intersection of the ray with the sphere
        oc = camera_pos - sphere_center
        b = 2 * np.dot(oc, ray_dir)
        c = np.dot(oc, oc) - sphere_radius * sphere_radius
        discriminant = b * b - 4 * c

        # These lines compute whether or not the viewing ray intersects with the sphere. This is done by solving a quadratic equation derived from substituting the parametric equation of a ray into the implicit equation of a sphere.

        # If the ray hit the sphere
        if discriminant > 0:
            t = (-b - np.sqrt(discriminant)) / 2

            # Compute the surface normal at the intersection point
            hit_pos = camera_pos + t * ray_dir
            normal = (hit_pos - sphere_center) / sphere_radius

            # Shade the pixel based on the angle between the normal and the light direction
            light_dir = np.array([0.5, -1, -1])
            light_dir /= np.linalg.norm(light_dir)  # Normalize
            intensity = max(0, np.dot(normal, -light_dir))

            # Write the color to the image
            image[y, x] = [intensity] * 3

            # If there is an intersection (i.e., if discriminant > 0), these lines compute shading for that pixel. The shading is computed based on Lambert’s cosine law which states that brightness is proportional to cosine of angle between surface normal and light direction.

# Display the image
plt.imshow(image)
plt.show()