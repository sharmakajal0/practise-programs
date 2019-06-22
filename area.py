#!/usr/bin/env python
## Find the area of a triangle whose perimeter is given

for _ in range(int(input())):
    n=int(input())
    side = n / 4
    area = side * side
    print(area, "sq. meter")

## Find cost of painting of wall if length and breath of wall and door is given.
l1, b1 = map(float, input().split())
l2, b2 = map(float, input().split())
cost = int(input())
area1 = l1 * b1
area2 = l2 * b2
if area1 > area2:
    area = area1 - area2
else:
    area = area2 - area1
price = area * cost
print(price)
