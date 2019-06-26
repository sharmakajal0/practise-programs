#!/usr/bin/env python

from cube import Cube
from sys import argv

def main(args):
    side = int(args[1])
    
    print("The side of the cube is %d" % (side), "units")

    c1 = Cube(side)
    print("The Lateral surface area of cube is ", c1.lateralSurfaceArea(), "sq. units")
    print("The Total surface area of cube is ", c1.totalSurfaceArea(), "sq. units")
    print("The volume of the cube is ", c1.volume(), "cubic units")

if __name__ == "__main__":
    main(argv)