import unittest
from lab4.pesel_validator.pesel_validator import PeselValidator

class TestPeselValidator(unittest.TestCase):
    def test_pesel_format(self):
        self.assertTrue(PeselValidator.validate_format("44051401359"))

    def test_check_digit(self):
        self.assertTrue(PeselValidator.validate_check_digit("44051401359"))
        self.assertFalse(PeselValidator.validate_check_digit("44051401358"))

    def test_birth_date(self):
        self.assertTrue(PeselValidator.validate_birth_date(
            "44051401359"))
        self.assertFalse(PeselValidator.validate_birth_date(
            "99133201359"))

    def test_gender(self):
        self.assertEqual(PeselValidator.get_gender("44051401359"),
                         "Mężczyzna")
        self.assertEqual(PeselValidator.get_gender("44051401382"),
                         "Kobieta")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
