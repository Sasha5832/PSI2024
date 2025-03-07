import unittest
from src.fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.fib_0 = Fibonacci(0)
        self.fib_1 = Fibonacci(1)
        self.fib_5 = Fibonacci(5)
        self.fib_10 = Fibonacci(10)

    def test_fibonacci_base_cases(self):
        self.assertEqual(self.fib_0.calculate(), 0)
        self.assertEqual(self.fib_1.calculate(), 1)

    def test_fibonacci_small_numbers(self):
        self.assertEqual(self.fib_5.calculate(), 5)

    def test_fibonacci_large_numbers(self):
        self.assertEqual(self.fib_10.calculate(), 55)

    def test_fibonacci_negative_number(self):
        with self.assertRaises(ValueError):
            Fibonacci(-1).calculate()

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
