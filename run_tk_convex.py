#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon
from r2vector import R2Vector


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
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
tk.clean(f.triangle)

try:
    while True:
        f = f.add(R2Point())
        tk.clean(f.triangle)
        f.draw(tk)
        angles = f.sum_angles()
        print(f"S = {f.area()}, P = {f.perimeter()}, "
              f"angles = {f.sum_angles()}\n")
except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
