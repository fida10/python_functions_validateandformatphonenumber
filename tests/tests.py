import unittest
from src.ans import format_phone_number


class TestFormatPhoneNumber(unittest.TestCase):

    def test_valid_phone_number(self):
        formatted = format_phone_number("1234567890")
        self.assertEqual(formatted, "(123) 456-7890")

    def test_invalid_phone_number(self):
        self.assertIsNone(format_phone_number("12345"))

    def test_non_numeric_phone_number(self):
        self.assertIsNone(format_phone_number("abcd"))


if __name__ == '__main__':
    unittest.main()
