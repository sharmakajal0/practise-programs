#!/usr/bin/env python

from rectangle import Rectangle
from sys import argv

def main(args):
    length = int(args[1])
    breadth = int(args[2])
    print("length and breadth of rectangle is %d and %d" % (length, breadth))

    r1 = Rectangle(length, breadth)
    print("Perimeter: ", r1.perimeter())
    print("Area: ", r1.area())

if __name__ == "__main__":
    main(argv)