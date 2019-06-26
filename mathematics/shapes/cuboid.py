from three_d_shapes import Three_d_Shapes

class Cuboid(Three_d_Shapes):
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def lateralSurfaceArea(self):
        return 4 * self.height * (self.length + self.breadth)

    def totalSurfaceArea(self):
        return 2 * (self.length * self.breadth + self.length * self.height + self.breadth * self.height)

    def volume(self):
        return self.length * self.breadth * self.height
