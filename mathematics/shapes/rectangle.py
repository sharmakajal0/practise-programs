from two_d_shape import TwoDimensionalShape

class Rectangle(TwoDimensionalShape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        return 2 * (self.length + self.breadth)

    def area(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        return self.length * self.breadth