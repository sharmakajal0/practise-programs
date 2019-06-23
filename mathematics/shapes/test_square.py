#!/usr/bin/env python

from square import Square
from sys import argv

def main(args):
    side = int(args[1])
    print("side of the square is %d" % (side))

    s1 = Square(side)
    print("Perimeter: ", s1.perimeter())
    print("Area: ", s1.area())

if __name__ == "__main__":
    main(argv)