from two_d_shape import TwoDimensionalShape

class Triangle(TwoDimensionalShape):
    def __init__(self, side1, side2, side3, height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height
    
    def perimeter(self):
        if self.side1 == self.side2 == self.side3:
            return 3 * self.side1
        elif self.side1 == self.side2 != self.side3:
            return 2 * self.side1 + self.side3
        else:
            return self.side1 + self.side2 + self.side3

    def area(self):
        return 0.5 * self.side1 * self.height