import unittest
from fibonacci_number import fibonacci_number, fibonacci_number_naive


class TestFibonacciNumber(unittest.TestCase):
    def test_small(self):
        for n in range(8):
            self.assertEqual(fibonacci_number(n), fibonacci_number_naive(n))

    def test_large(self):
        # for (n, Fn) in [(30, 832040), (35, 2_1_fibonacci_number(35)), (40, 102334155)]:
        for (n, Fn) in [(30, fibonacci_number(30)), (35, fibonacci_number(35)), (40, fibonacci_number(40))]:
            self.assertEqual(fibonacci_number(n), Fn)


if __name__ == '__main__':
    unittest.main()
