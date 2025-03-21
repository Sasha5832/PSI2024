import re
from datetime import datetime

class PeselValidator:
    def __init__(self, pesel):
        self.pesel = pesel

    @staticmethod
    def validate_format(pesel):
        return bool(re.fullmatch(r"\d{11}", pesel))

    @staticmethod
    def validate_check_digit(pesel):
        if not PeselValidator.validate_format(pesel):
            return False

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        check_sum = sum(int(pesel[i]) * weights[i] for i in range(10))
        control_digit = (10 - (check_sum % 10)) % 10
        return control_digit == int(pesel[10])

    @staticmethod
    def validate_birth_date(pesel):
        if not PeselValidator.validate_format(pesel):
            return False

        year = int(pesel[:2])
        month = int(pesel[2:4])
        day = int(pesel[4:6])

        if 1 <= month <= 12:
            year += 1900
        elif 21 <= month <= 32:
            year += 2000
            month -= 20
        elif 41 <= month <= 52:
            year += 2100
            month -= 40
        elif 61 <= month <= 72:
            year += 2200
            month -= 60
        elif 81 <= month <= 92:
            year += 1800
            month -= 80
        else:
            return False

        try:
            datetime(year, month, day)
            return True
        except ValueError:
            return False

    @staticmethod
    def get_gender(pesel):
        if not PeselValidator.validate_format(pesel):
            return None

        return "Mężczyzna" if int(pesel[9]) % 2 == 1 else "Kobieta"