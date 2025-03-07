import unittest
from src.StringManipulator import StringManipulator

class TestStringManipulator(unittest.TestCase):

    def setUp(self):
        self.manipulator = StringManipulator("hello world")
        self.manipulator2 = StringManipulator("hello world2@")

    def test_reverse_string(self):
        self.assertEqual(self.manipulator.reverse_string(), "dlrow olleh")

    def test_reverse_string2(self):
        self.assertEqual(self.manipulator2.reverse_string(), "@2dlrow olleh")

    def test_count_words(self):
        self.assertEqual(self.manipulator.count_words(), 2)

    def test_capitalize_words(self):
        self.assertEqual(self.manipulator.capitalize_words(), "Hello World")

    def test_capitalize_words2(self):
        self.assertEqual(self.manipulator2.capitalize_words(), "Hello World2@")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
