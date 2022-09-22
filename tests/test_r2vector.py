from pytest import approx
from math import sqrt
from r2point import R2Point
from r2vector import R2Vector


class TestR2Vector:

    def setup_method(self):
        self.v = R2Vector(R2Point(0.0, 0.0), R2Point(1.0, 1.0))

    def test_module1(self):
        assert self.v.module() == sqrt(2)

    def test_module2(self):
        assert R2Vector(R2Point(0.0, 0.0), R2Point(5.0, 0.0)).module() == 5

    def test_scalar1(self):
        assert R2Vector.scalar_composition(self.v,
                                           R2Vector(R2Point(0.0, 0.0),
                                                    R2Point(1.0, 0.0))) == 1

    def test_scalar2(self):
        assert R2Vector.scalar_composition(self.v,
                                           R2Vector(R2Point(0.0, 0.0),
                                                    R2Point(0.0, 1.0))) == 1

    def test_scalar3(self):
        assert R2Vector.scalar_composition(self.v,
                                           R2Vector(R2Point(0.0, 0.0),
                                                    R2Point(1.0, 0.5))) == 1.5

    def test_scalar4(self):
        assert R2Vector.scalar_composition(self.v,
                                           R2Vector(R2Point(0.0, 1.0),
                                                    R2Point(1.0, 0.0))) == 0

    def test_vector1(self):
        assert self.v.vector_composition(R2Vector(R2Point(0.0, 0.0),
                                                  R2Point(0.0, 1.0))) == 1

    def test_vector2(self):
        assert self.v.vector_composition(R2Vector(R2Point(0.0, 0.0),
                                                  R2Point(1.0, 0.0))) == -1

    def test_vector3(self):
        assert self.v.vector_composition(R2Vector(R2Point(-1.0, -1.0),
                                                  R2Point(2.0, 2.0))) == 0

    def test_intersect1(self):
        assert self.v.is_intersect(R2Vector(R2Point(0.0, 0.0),
                                            R2Point(0.0, 1.0))) is True

    def test_intersect2(self):
        assert self.v.is_intersect(R2Vector(R2Point(1.0, 0.0),
                                            R2Point(0.0, 1.0))) is True

    def test_intersect3(self):
        assert self.v.is_intersect(R2Vector(R2Point(0.0, 0.5),
                                            R2Point(0.0, 1.0))) is False

    def test_intersect4(self):
        assert self.v.is_intersect(R2Vector(R2Point(-1.0, -1.0),
                                            R2Point(0.5, 0.5))) is True

    def test_intersect5(self):
        assert R2Vector(R2Point(1.0, 0.0),
                        R2Point(0.0, 1.0)).is_intersect(
            R2Vector(R2Point(1.5, 0.0),
                     R2Point(0.5, -1.0))) is False

    def test_degree1(self):
        assert self.v.degree(R2Vector(R2Point(0.0, 0.0), R2Point(0.0, 1.0))) \
               == approx(45)

    def test_degree2(self):
        assert self.v.degree(R2Vector(R2Point(0.5, 0.0), R2Point(1.0, 0.0))) \
               == 0

    def test_degree3(self):
        assert self.v.degree(R2Vector(R2Point(1.0, 0.0), R2Point(0.0, 1.0))) \
                == approx(90)

    def test_degree4(self):
        assert self.v.degree(R2Vector(R2Point(-1.0, -1.0),
                                      R2Point(0.5, 0.5))) == 0

    def test_degree5(self):
        assert R2Vector(R2Point(1.0, 0.0),
                        R2Point(0.0, 1.0)).degree(
            R2Vector(R2Point(1.5, 0.0),
                     R2Point(0.5, -1.0))) == 0
