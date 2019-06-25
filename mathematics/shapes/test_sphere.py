from sphere import Sphere
from sys import argv

def main(args):
    radius = int(args[1])

    print("The radius of the sphere is %d" % (radius))
    s1 = Sphere(radius)
    print("The surface area of sphere is ", s1.surfaceArea())
    print("The volume of sphere is ", s1.volume())

if __name__ == "__main__":
    main(argv)