from typing import Tuple

def _fib_fast_doubling(n: int) -> Tuple[int, int]:
    """Returns (F(n), F(n+1)) using fast doubling."""
    if n == 0:
        return 0, 1
    a, b = _fib_fast_doubling(n >> 1)
    c = a * ((b << 1) - a)
    d = a * a + b * b
    if n & 1:
        return d, c + d
    else:
        return c, d

def solution_station_1(x: int) -> int:
    """Return F(x) with F(0)=0, F(1)=1."""
    if x < 0:
        raise ValueError("Station 1 expects a non-negative integer.")
    return _fib_fast_doubling(x)[0]
