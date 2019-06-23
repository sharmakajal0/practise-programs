from two_d_shape import TwoDimensionalShape

class Square(TwoDimensionalShape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side * self.side