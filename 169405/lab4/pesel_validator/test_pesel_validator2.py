import unittest
from pesel_validator import PeselValidator

class TestPeselValidator(unittest.TestCase):
    def test_pesel_format(self):
        self.assertTrue(PeselValidator.validate_format("44051401359"))  # poprawny format
        self.assertFalse(PeselValidator.validate_format("12345"))  # za krótki
        self.assertFalse(PeselValidator.validate_format("abcdef12345"))  # nie tylko cyfry
        self.assertFalse(PeselValidator.validate_format("123456789012"))  # za długi

    def test_check_digit(self):
        self.assertTrue(PeselValidator.validate_check_digit("44051401359"))  # poprawny PESEL
        self.assertFalse(PeselValidator.validate_check_digit("44051401358"))  # błędna cyfra kontrolna

    def test_birth_date(self):
        self.assertTrue(PeselValidator.validate_birth_date("44051401359"))  # poprawna data
        self.assertFalse(PeselValidator.validate_birth_date("99133101359"))  # niepoprawna data

    def test_gender(self):
        self.assertEqual(PeselValidator.get_gender("44051401359"), "M")  # mężczyzna
        self.assertEqual(PeselValidator.get_gender("44051401426"), "K")  # kobieta

    def test_is_valid(self):
        self.assertTrue(PeselValidator.is_valid("44051401359"))  # poprawny PESEL
        self.assertFalse(PeselValidator.is_valid("99133101359"))  # błędna data
        self.assertFalse(PeselValidator.is_valid("44051401358"))  # błędna cyfra kontrolna

    def test_leap_year(self):
        self.assertTrue(PeselValidator.validate_birth_date("00222901359"))  # 29 lutego 2000 (przestępny)
        self.assertFalse(PeselValidator.validate_birth_date("01022901359"))  # 29 lutego 2001 (nieprzestępny)

if __name__ == "__main__":
    unittest.main()
