from deq import Deq
from r2point import R2Point
from r2vector import R2Vector


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0

    def sum_angles(self):
        return 0.0


class Void(Figure):
    """ "Hульугольник" """
    def __init__(self, triangle):
        self.triangle = triangle

    def add(self, p):
        return Point(p, self.triangle)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p, triangle):
        self.p = p
        self.triangle = triangle

    def add(self, q):
        return self if self.p == q else Segment(self.p, q, self.triangle)


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q, triangle):
        self.p, self.q = p, q
        self.triangle = triangle

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r, self.triangle)
        elif self.q.is_inside(self.p, r):
            return Segment(self.p, r, self.triangle)
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q, self.triangle)
        else:
            return self

    def sum_angles(self):
        return 2 * sum(R2Vector(self.p, self.q).degree(
            self.triangle[i]) for i in range(3))


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c, triangle):
        self.triangle = triangle
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))
        self.angles = Deq()
        for i in range(3):
            self.angles.push_last(sum(
                R2Vector(self.points.array[i-1], self.points.array[i]).degree(
                    self.triangle[j]) for j in range(3)))

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())
            self.angles.push_last(self.angles.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))
            a = self.angles.pop_first()

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            a = self.angles.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                p = self.points.pop_first()
                a = self.angles.pop_first()
            self.points.push_first(p)
            self.angles.push_first(a)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            a = self.angles.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))
                p = self.points.pop_last()
                a = self.angles.pop_last()
            self.points.push_last(p)
            self.angles.push_last(a)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            self.angles.push_first(sum(
                R2Vector(self.points.first(),
                         t).degree(self.triangle[i]) for i in range(3)))
            self.points.push_first(t)
            self.angles.push_first(sum(
                R2Vector(self.points.first(),
                         self.points.last()).degree(self.triangle[i])
                for i in range(3)))

        return self

    def sum_angles(self):
        return sum(self.angles.array)


if __name__ == "__main__":
    triangle = [R2Vector(R2Point(0.0, 1.0), R2Point(0.0, 0.0)),
                R2Vector(R2Point(0.0, 0.0), R2Point(1.0, 0.0)),
                R2Vector(R2Point(1.0, 0.0), R2Point(0.0, 1.0))]
    f = Void(triangle)
    f = f.add(R2Point(0.5, 0.0))
    f = f.add(R2Point(0.5, 1.0))
    f = f.add(R2Point(1.0, 1.0))
    f = f.add(R2Point(1.0, 0.0))
    f = f.add(R2Point(0.0, 1.0))
    angles = f.sum_angles()
    print(angles)
