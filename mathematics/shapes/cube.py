from three_d_shapes import Three_d_Shapes

class Cube(Three_d_Shapes):
    def __init__(self, side):
        self.side = side

    def lateralSurfaceArea(self):
        return 4 * self.side * self.side

    def totalSurfaceArea(self):
        return 6 * self.side * self.side

    def volume(self):
        return self.side * self.side * self.side
