#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void
from r2vector import R2Vector

print('Введите координаты вершин треугольника:')
x1 = float(input('x -> '))
y1 = float(input('y -> '))
x2 = float(input('x -> '))
y2 = float(input('y -> '))
x3 = float(input('x -> '))
y3 = float(input('y -> '))
triangle = [R2Vector(R2Point(x1, y1), R2Point(x2, y2)),
            R2Vector(R2Point(x2, y2), R2Point(x3, y3)),
            R2Vector(R2Point(x1, y1), R2Point(x3, y3))]
print('Введите координаты точек выпуклой оболочки:')
f = Void(triangle)
try:
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, angle = {f.sum_angles()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
