#!/usr/bin/env python

from triangle import Triangle
from sys import argv

def main(args):
    side1 = int(args[1])
    side2 = int(args[2])
    side3 = int(args[3])
    height = int(args[4])
    
    print("the three sides and height of triangle area %d %d %d and %d" %(side1, side2, side3, height))
    t1 = Triangle(side1, side2, side3, height)
    print("Perimeter: ", t1.perimeter())
    print("Area: ", t1.area())

if __name__ == "__main__":
    main(argv)