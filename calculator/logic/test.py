import unittest
from logic import Number, DigitOutOfRangeException, Calculator, operators


class NumberTest(unittest.TestCase):
    def test_NumberStartsAtZero(self):
        num = Number()
        self.assertEqual(num.value, 0)

    def test_addDigitCorrectlyGoesFrom0To4(self):
        num = Number()
        num.add_digit(4)
        self.assertEqual(num.value, 4)

    def test_addDigitCorrectlyGoesFrom0To3To36(self):
        num = Number()
        num.add_digit(3)
        num.add_digit(6)
        self.assertEqual(num.value, 36)

    def test_addDigitCorrectlyGoesFrom0To3To30To309(self):
        num = Number()
        num.add_digit(3)
        self.assertEqual(num.value, 3)
        num.add_digit(0)
        self.assertEqual(num.value, 30)
        num.add_digit(9)
        self.assertEqual(num.value, 309)

    def test_addDigitDoesNotChangeWhenGiven0AsTheFirstDigit(self):
        num = Number()
        num.add_digit(0)
        self.assertEqual(num.value, 0)

    def test_addDigitThrowsExceptionWhenGivenToLargeAnInteger(self):
        num = Number()
        with self.assertRaises(DigitOutOfRangeException):
            num.add_digit(10)

    def test_addDigitThrowsExceptionWhenGivenToSmallAnInteger(self):
        num = Number()
        with self.assertRaises(DigitOutOfRangeException):
            num.add_digit(-1)

    def test_removeDigitGoesFrom309To30To3To0(self):
        num = Number()
        num.add_digit(3)
        self.assertEqual(num.value, 3)
        num.add_digit(0)
        self.assertEqual(num.value, 30)
        num.add_digit(9)
        self.assertEqual(num.value, 309)
        num.remove_digit()
        self.assertEqual(num.value, 30)
        num.remove_digit()
        self.assertEqual(num.value, 3)
        num.remove_digit()
        self.assertEqual(num.value, 0)


class CalculatorTest(unittest.TestCase):
    def test_twoPlusFourteenEqualsSixteen(self):
        calc = Calculator()
        calc.add_digit(2)
        calc.set_operation(operators["+"])
        calc.add_digit(1)
        calc.add_digit(4)
        self.assertEqual(calc.get_result(), 16)

    def test_twoMinusFourteenEqualsNegativeTwelve(self):
        calc = Calculator()
        calc.add_digit(2)
        calc.set_operation(operators["-"])
        calc.add_digit(1)
        calc.add_digit(4)
        self.assertEqual(calc.get_result(), -12)


if __name__ == '__main__':
    unittest.main()
