#!/usr/bin/env python

## areas of various shapes

from math import pi
def area_of_triangle():
    print("base and height of triangle")
    base, height = map(int, input().split())
    return 0.5 * base * height

def area_of_circle():
    print("radius of circle")
    radius = int(input())
    return pi * radius * radius

def area_of_square():
    print("side of square")
    side = int(input())
    return side * side

def area_of_rectangle():
    print("length and breadth of rectangle")
    length, breadth = map(int, input().split())
    return length * breadth

def area_of_parallelogram():
    print("base and height of parallelogram")
    base, height = map(int, input().split())
    return base * height


print(area_of_triangle())
print(area_of_circle())
print(area_of_parallelogram())
print(area_of_rectangle())
print(area_of_square())