import unittest
from src.calkulator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Ten kod jest wykonywany przed każdym testem
        self.calculator = Calculator(10, 2)

    def test_add(self):
        self.assertEqual(self.calculator.add(), 10+2)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(), 10-2)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(), 10*2)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(), 10/2)


    def tearDown(self):
        # Ten kod jest wykonywany po każdym teście
        pass


if __name__ == "__main__":
    unittest.main()