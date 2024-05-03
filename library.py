import numpy as np
from functools import cache


@cache
def factorial(n):
    return n * factorial(n-1) if n != 1 else 1


@cache
def sum_factorials(n: int):
    return factorial(n) + sum_factorials(n - 1) if n != 1 else 1


def arithmetic_sum(n: int) -> int:  # problem 1
    return int(0.5 * n * (n + 1))


@cache
def fib(m):  # problem 2
    return fib(m - 1) + fib(m - 2) if m > 2 else m


def prime_factors(n):  # problem 3
    """Simple distinct prime factor tracker"""
    p = []
    q = 2
    while q <= np.sqrt(n):
        if n % q == 0:
            is_prime = True
            for f in p:
                if q % f == 0:
                    is_prime = False
            if is_prime:
                p.append(q)
        q += 1
    return p
