#!/usr/bin/env python

from circle import Circle
from sys import argv

def main(args):
    radius = int(args[1])

    print("radius: ", radius)
    print("Creating circle of Radius = %s" % (radius))
    
    c1 = Circle(radius)
    
    print("Perimeter: ", c1.perimeter())
    print("Area: ", c1.area())

if __name__ == "__main__":
    main(argv)