"""Input validation helpers."""


def parse_float(text: str) -> float:
    return float(text.strip())


def parse_integer(text: str) -> int:
    return int(text.strip())
