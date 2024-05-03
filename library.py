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


def divisor_power(p, n):  # problem 5
    """Find the greatest power of p that divides n."""
    i = 0
    while n % p == 0:
        i += 1
        n = n / p
    return i


def known_divisor(q, factors):  # problem 5
    """Check whether q has a factor in factors."""
    is_known = True
    for f in factors:
        if q % f == 0:
            is_known = False
    return is_known


def prime_factors(n):  # problem 5
    """Simple distinct prime factor tracker."""
    p = {}
    # primes are naturals greater than 2
    if n < 2:
        pass
    else:
        # test for factors
        q = 2
        while q <= n / 2:
            if n % q == 0:
                if known_divisor(q, p):
                    p[q] = divisor_power(q, n)
            q += 1
        # no factors means that n is a prime
        if len(p) == 0:
            p = {n: 1}
    return p


def is_palindrome(n):  # problem 4
    return str(n) == str(n)[::-1]


def search_largest_palindrome(n):  # problem 4
    best = 1
    for i in range(n + 1)[::-1]:
        for j in range(n + 1)[::-1]:
            if i * j <= best:
                pass
            elif is_palindrome(i * j):
                best = i * j
    return best

