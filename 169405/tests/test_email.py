import unittest
from src.email import validate_email


class TestEmail(unittest.TestCase):

    def setUp(self):
        pass
        #self.calculator = validate_email("sasha@.gmail.com")

    def test_validate_positive(self):
        self.assertEqual(validate_email("inf@onet.pl"), True)

    def test_validate_negative(self):
        self.assertFalse(validate_email("asdfa"), True)

    def test_integer_argument(self):
        with self.assertRaises(TypeError):
            validate_email(123)


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()