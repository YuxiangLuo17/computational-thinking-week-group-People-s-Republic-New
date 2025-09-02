# station2.py
import re
from datetime import date

def solution_station_2(x: str) -> str:
    """
    Given a date string like '2024 - 08 - 06' (whitespace and hyphens may vary),
    return the weekday name in lowercase, e.g., 'tuesday'.
    """
    # Extract year, month, day as integers regardless of spaces/hyphens
    nums = list(map(int, re.findall(r"\d+", x)))
    if len(nums) != 3:
        raise ValueError(f"Expected a date string with Y, M, D. Got: {x!r}")
    y, m, d = nums
    return date(y, m, d).strftime("%A").lower()
