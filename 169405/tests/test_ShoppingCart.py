import unittest
from src.ShoppingCart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.emptycard = ShoppingCart([])
        self.card = ShoppingCart(["Apple", "orange"])

    def test_add_positive(self):
        self.emptycard.add_item("Bread")
        s1= ShoppingCart(["Blead"])
        self.assertEqual(self.emptycard, s1)

    def test_string_representation(self):
        self.assertEqual(str(self.card), "Shopping card: ['Apple', 'orange'].")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()