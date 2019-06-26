#!/usr/bin/env python

from cuboid import Cuboid
from sys import argv

def main(args):
    length = int(args[1])
    breadth = int(args[2])
    height = int(args[3])

    print("The length, breadth and height of cuboid are %d, %d and %d" % (length, breadth, height), "units")
    
    cu1 = Cuboid(length, breadth, height)
    print("Lateral Surface Area ", cu1.lateralSurfaceArea(), "sq. units")
    print("Total Surface Area ", cu1.totalSurfaceArea(), "sq. units")
    print("volume ", cu1.volume(), "cubic units")

if __name__ == "__main__":
    main(argv)
