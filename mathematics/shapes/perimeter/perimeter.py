#!/usr/bin/env python

## perimeter of various shapes

from math import pi
def square_perimeter():
    print("side of square")
    side = int(input())
    return 4 * side

def circle_perimeter():
    print("radius of circle")
    radius = int(input())
    return 2 * pi * radius

def triangle_perimeter():
    print("three sides of triangle")
    a, b, c = map(int, input().split())
    if a == b == c:
        return 3 * a
    elif a == b != c:
        return (2 * a) + c
    else:
        return a + b + c

def rectangle_perimeter():
    print("length and breadth of rectangle")
    length, breadth = map(int, input().split())
    return 2 * (length + breadth)

print(triangle_perimeter())
print(square_perimeter())
print(circle_perimeter())
print(rectangle_perimeter())

