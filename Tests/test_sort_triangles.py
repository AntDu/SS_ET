from unittest import TestCase

from Sort_triangles import Triangle
from Sort_triangles import triangle_is_exist
from Sort_triangles import triangle_is_valid


class TestTriangle(TestCase):

    def test_area_calculation(self):
        result = round(Triangle.area(3.7, 4.2, 6.5), 2)
        self.assertEqual(result, 7.27)

    def test_triangle_is_valid(self):

        self.assertTrue(triangle_is_valid('triangle', 3.7, 4.2, 6.5))

    def triangle_is_exist(self):

        self.assertTrue(triangle_is_exist(3.7, 5.0, 11.0))


if __name__ == '__main__':
    TestTriangle()

