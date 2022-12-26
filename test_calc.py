import pytest


from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 4

    def test_subtraction_success(self):
        assert self.calc.subtraction(2, 1) == 1

    def test_division_success(self):
        assert self.calc.division(4, 2) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(2, 3) == 6
