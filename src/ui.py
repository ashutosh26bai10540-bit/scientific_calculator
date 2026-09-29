"""Console user interface for the scientific calculator."""
from .calculator import calculate_choice
from .menu import display_menu
from .validators import parse_float, parse_integer


def run() -> None:
    display_menu()
    while True:
        choice = input("\nEnter your choice: ").strip()
        if choice == "12":
            print("Thank you for using the calculator!")
            break
        try:
            if choice in {"1", "2", "3", "4", "5"}:
                num1 = parse_float(input("Enter first number: "))
                num2 = parse_float(input("Enter second number: "))
                result = calculate_choice(choice, [num1, num2])
            elif choice == "8":
                num = parse_integer(input("Enter a number: "))
                result = calculate_choice(choice, [float(num)])
            elif choice in {"6", "7", "9", "10", "11"}:
                num = parse_float(input("Enter a number: "))
                result = calculate_choice(choice, [num])
            else:
                print("Invalid choice. Please try again.")
                continue
            print("Result:", result)
        except (ValueError, ZeroDivisionError, OverflowError) as exc:
            print(str(exc) or "Please enter a valid number.")
