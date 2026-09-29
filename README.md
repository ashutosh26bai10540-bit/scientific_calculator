# Scientific Calculator

## Overview
A modular Python command-line scientific calculator that performs arithmetic and scientific calculations through a clear menu-driven interface. The implementation separates the user interface, validation, arithmetic operations, scientific operations, and menu logic.

## Features
- Addition, subtraction, multiplication, division
- Power and square operations
- Square root with negative-input validation
- Factorial with negative-input validation
- Sine, cosine, and tangent using degree input
- Division-by-zero protection
- Invalid-input handling
- Modular source structure
- Automated pytest test suite

## Technologies
- Python 3.10+
- Python standard library (`math`)
- Pytest for testing
- Git for version control

## Project Structure
```text
Scientific_Calculator_VITyarthi/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── calculator.py
│   ├── operations.py
│   ├── scientific.py
│   ├── validators.py
│   ├── menu.py
│   └── ui.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── docs/
│   ├── diagrams/
│   └── screenshots/
├── requirements.txt
├── README.md
└── statement.md
```

## How to Run
1. Install Python 3.10 or newer.
2. Open a terminal in the project folder.
3. Run:
   `python -m src.main`
4. Select an operation and enter the requested values.

## Testing
Install pytest if needed:
`python -m pip install -r requirements.txt`

Run:
`python -m pytest -q`

## GitHub
Create an empty GitHub repository and push the local `main` branch. See `GITHUB_PUSH.md` for the exact commands.
