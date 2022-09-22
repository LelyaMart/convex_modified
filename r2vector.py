from math import sqrt, acos, degrees
from r2point import R2Point


class R2Vector:

    def __init__(self, first, second):
        self.first, self.second = first, second
        self.x = self.second.x - self.first.x
        self.y = self.second.y - self.first.y

    @staticmethod
    def scalar_composition(a, b):
        return a.x * b.x + a.y * b.y

    def module(self):
        return sqrt(R2Vector.scalar_composition(self, self))

    def degree(self, other):
        if self.is_intersect(other) and self.module() != 0 and \
                other.module != 0:
            return degrees(acos(abs(R2Vector.scalar_composition(self, other))
                                / self.module() / other.module()))
        return 0.0

    def vector_composition(self, other):
        return self.x * other.y - self.y * other.x

    def is_intersect(self, other):
        z1 = R2Vector(self.first, other.second).vector_composition(self)
        z2 = R2Vector(self.first, other.first).vector_composition(self)
        z3 = R2Vector(other.first, self.first).vector_composition(other)
        z4 = R2Vector(other.first, self.second).vector_composition(other)

        return z1 * z2 <= 0 and z3 * z4 <= 0
