"""Scientific operations used by the calculator."""
import math


def square_root(value: float) -> float:
    if value < 0:
        raise ValueError("Square root of a negative number is not possible.")
    return math.sqrt(value)


def factorial(value: int) -> int:
    if value < 0:
        raise ValueError("Factorial cannot be calculated for a negative number.")
    return math.factorial(value)


def sin_degrees(angle: float) -> float:
    return math.sin(math.radians(angle))


def cos_degrees(angle: float) -> float:
    return math.cos(math.radians(angle))


def tan_degrees(angle: float) -> float:
    return math.tan(math.radians(angle))
