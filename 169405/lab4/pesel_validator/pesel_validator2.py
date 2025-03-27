import re
from datetime import datetime

class PeselValidator:
    """Klasa do walidacji numerów PESEL."""

    @staticmethod
    def validate_format(pesel: str) -> bool:
        """Sprawdza, czy PESEL składa się dokładnie z 11 cyfr."""
        return bool(re.fullmatch(r"\d{11}", pesel))

    @staticmethod
    def validate_check_digit(pesel: str) -> bool:
        """Sprawdza poprawność cyfry kontrolnej PESEL."""
        if not PeselValidator.validate_format(pesel):
            return False
        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        check_sum = sum(int(pesel[i]) * weights[i] for i in range(10))
        check_digit = (10 - (check_sum % 10)) % 10
        return check_digit == int(pesel[10])

    @staticmethod
    def validate_birth_date(pesel: str) -> bool:
        """Dekoduje datę urodzenia z numeru PESEL."""
        if not PeselValidator.validate_format(pesel):
            return False

        year = int(pesel[:2])
        month = int(pesel[2:4])
        day = int(pesel[4:6])

        # Określenie stulecia na podstawie miesiąca
        if 1 <= month <= 12:
            century = 1900
        elif 21 <= month <= 32:
            century = 2000
            month -= 20
        elif 41 <= month <= 52:
            century = 2100
            month -= 40
        elif 61 <= month <= 72:
            century = 2200
            month -= 60
        elif 81 <= month <= 92:
            century = 1800
            month -= 80
        else:
            return False  # Niepoprawny miesiąc

        full_year = century + year

        try:
            return datetime(full_year, month, day)is not None
        except ValueError:
            return False


    @staticmethod
    def get_gender(pesel: str) -> str:
        """Określa płeć na podstawie numeru PESEL (cyfra na 10. pozycji: parzysta - K, nieparzysta - M)."""
        return "M" if int(pesel[9]) % 2 else "K"

    @staticmethod
    def is_valid(pesel: str) -> bool:
        """Sprawdza pełną poprawność numeru PESEL."""
        return (
            PeselValidator.validate_format(pesel) and
            PeselValidator.validate_birth_date(pesel) and
            PeselValidator.validate_check_digit(pesel)
        )

if __name__ == "__main__":
    pesel = input("Podaj PESEL: ")
    if PeselValidator.is_valid(pesel):
        print("PESEL poprawny!")
    else:
        print("PESEL niepoprawny!")
