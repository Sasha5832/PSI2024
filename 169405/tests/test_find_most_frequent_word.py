import unittest
from src.find_most_frequent_word import WordAnalyzer

class TestWordAnalyzer(unittest.TestCase):

    def setUp(self):
        self.empty_text = WordAnalyzer("")
        self.single_word = WordAnalyzer("hello")
        self.repeated_word = WordAnalyzer("hello hello world")
        self.equal_frequency = WordAnalyzer("apple banana apple banana")

    def test_empty_text(self):
        self.assertIsNone(self.empty_text.find_most_frequent_word())

    def test_single_word(self):
        self.assertEqual(self.single_word.find_most_frequent_word(), "hello")

    def test_repeated_word(self):
        self.assertEqual(self.repeated_word.find_most_frequent_word(), "hello")

    def test_equal_frequency(self):
        self.assertIn(self.equal_frequency.find_most_frequent_word(), ["apple", "banana"])

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
