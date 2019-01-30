from unittest import TestCase

from Fibonacci_series import Fibonacci


class TestFibonacci(TestCase):

    def test_fibonacci_num_from_1_to_5(self):
        first = 0
        last = 5
        fr = Fibonacci.fib(first, last)
        self.assertEqual(fr, [0, 1, 1, 2, 3, 5])

    def test_fibonacci_num_from_6_to_110(self):
        first = 6
        last = 110
        fr = Fibonacci.fib(first, last)
        self.assertEqual(fr, [8, 13, 21, 34, 55, 89])


if __name__ == '__main__':
    TestFibonacci()
