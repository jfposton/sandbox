class Calculator:
    def __init__(self):
        self.operator = None
        self.A = None
        self.B = None

    def add_digit(self, digit):
        """
        Add a digit to the current number by placing the provided digit in the ones place
        and shifting the rest of the numbers to the left by one place.

        :param digit: int Integer value between 0 and 9
        :return: None
        """
        if 0 <= digit <= 9:
            if self.operator is None:
                if self.A is None:
                    self.A = Number()
                self.A.add_digit(digit)
            else:
                if self.B is None:
                    self.B = Number()
                self.B.add_digit(digit)
        else:
            raise DigitOutOfRangeException()

    def delete_digit(self):
        """
        Remove the last entered digit
        :return:
        """
        if self.operator is None:
            if self.A is not None:
                self.A.remove_digit()
        elif self.B is not None:
            self.B.remove_digit()

    def set_operation(self, operator):
        """
        Establishes what operation will be performed on the number currently entered
        with the subsequently entered number as a parameter.

        :param operator: operators.Operator
        :return: int
        """
        self.operator = operator

    def valid(self):
        return self.operator is not None and self.A is not None and self.B is not None

    def get_result(self):
        """
        Perform the operation specified on the two entered numbers. Will raise an exception
        if all parameters are not provided.
        :return: int
        """
        if self.valid():
            return self.operator(self.A, self.B)


class Number:
    def __init__(self):
        self.value = 0
        self.PLACE_MULTIPLIER = 10

    def add_digit(self, digit):
        if 0 > digit or digit > 9:
            raise DigitOutOfRangeException()
        self.value *= self.PLACE_MULTIPLIER
        self.value += digit

    def remove_digit(self):
        self.value /= self.PLACE_MULTIPLIER


class DigitOutOfRangeException(Exception):
    def __init__(self):
        super(DigitOutOfRangeException, self).__init__("Digit must be between 0 and 9")


operators = {
    "+": lambda a, b: a.value + b.value,
    "-": lambda a, b: a.value - b.value
}
