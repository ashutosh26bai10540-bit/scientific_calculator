import math
import pytest

from src import operations, scientific
from src.calculator import calculate_choice


def test_basic_operations():
    assert operations.add(2, 3) == 5
    assert operations.subtract(7, 2) == 5
    assert operations.multiply(4, 3) == 12
    assert operations.divide(10, 2) == 5
    assert operations.power(2, 4) == 16


def test_square_and_root():
    assert operations.square(5) == 25
    assert scientific.square_root(49) == 7


def test_factorial():
    assert scientific.factorial(5) == 120
    with pytest.raises(ValueError):
        scientific.factorial(-1)
    with pytest.raises(ValueError):
        calculate_choice("8", [5.5])


def test_trigonometry_in_degrees():
    assert math.isclose(scientific.sin_degrees(90), 1.0, abs_tol=1e-12)
    assert math.isclose(scientific.cos_degrees(0), 1.0, abs_tol=1e-12)
    assert math.isclose(scientific.tan_degrees(45), 1.0, abs_tol=1e-12)


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        operations.divide(10, 0)


def test_choice_dispatch():
    assert calculate_choice("1", [4, 6]) == 10
    assert calculate_choice("6", [5]) == 25
    assert math.isclose(calculate_choice("9", [90]), 1.0, abs_tol=1e-12)
