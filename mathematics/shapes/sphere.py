from three_d_shapes import Three_d_Shapes
from math import pi

class Sphere(object):
    def __init__(self, radius):
        self.radius = radius

    def surfaceArea(self):
        return 4 * pi * self.radius * self.radius

    def volume(self):
        return (4 * pi * self.radius * self.radius * self.radius) / 3
