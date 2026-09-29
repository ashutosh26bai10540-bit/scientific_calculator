"""Application service that connects menu choices to calculator operations."""
from . import operations, scientific


def calculate_choice(choice: str, values: list[float]) -> float | str:
    """Return a calculation result or a user-facing validation message."""
    if choice == "1":
        return operations.add(values[0], values[1])
    if choice == "2":
        return operations.subtract(values[0], values[1])
    if choice == "3":
        return operations.multiply(values[0], values[1])
    if choice == "4":
        return operations.divide(values[0], values[1])
    if choice == "5":
        return operations.power(values[0], values[1])
    if choice == "6":
        return operations.square(values[0])
    if choice == "7":
        return scientific.square_root(values[0])
    if choice == "8":
        if not values[0].is_integer():
            raise ValueError("Factorial requires an integer.")
        return scientific.factorial(int(values[0]))
    if choice == "9":
        return scientific.sin_degrees(values[0])
    if choice == "10":
        return scientific.cos_degrees(values[0])
    if choice == "11":
        return scientific.tan_degrees(values[0])
    raise ValueError("Invalid choice. Please try again.")
