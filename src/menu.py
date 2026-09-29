"""Menu definitions and display helpers."""

MENU = {
    "1": "Addition",
    "2": "Subtraction",
    "3": "Multiplication",
    "4": "Division",
    "5": "Power",
    "6": "Square",
    "7": "Square Root",
    "8": "Factorial",
    "9": "Sin",
    "10": "Cos",
    "11": "Tan",
    "12": "Exit",
}


def display_menu() -> None:
    print("===== SCIENTIFIC CALCULATOR =====")
    for key, label in MENU.items():
        print(f"{key}. {label}")
