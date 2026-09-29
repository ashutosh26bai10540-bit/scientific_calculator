# System Architecture

The calculator uses a small layered modular architecture:

- **UI layer (`ui.py`)**: displays the menu, reads user input, and prints results/errors.
- **Validation layer (`validators.py`)**: converts textual input into numeric types.
- **Application layer (`calculator.py`)**: dispatches a menu choice to the appropriate operation.
- **Operation layer (`operations.py`, `scientific.py`)**: performs arithmetic and scientific calculations.
- **Menu module (`menu.py`)**: stores menu definitions and renders the menu.
- **Entry point (`main.py`)**: starts the application.

This separation keeps calculation logic independently testable and keeps the user interface thin.
