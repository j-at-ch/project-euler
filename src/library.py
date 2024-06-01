from functools import cache
import numpy as np
from typing import Tuple


@cache
def factorial(n: int) -> int:
    return n * factorial(n-1) if n > 1 else 1


@cache
def sum_factorials(n: int) -> int:
    return factorial(n) + sum_factorials(n - 1) if n > 1 else 1


def arithmetic_sum(n: int) -> int:  # problem 1
    return int(0.5 * n * (n + 1))


@cache
def fibonacci(m):
    assert m >= 0
    return fibonacci(m - 1) + fibonacci(m - 2) if m > 2 else 1


def divisor_power(p, n):  # problem 5
    """Find the greatest power of p that divides n."""
    i = 0
    while n % p == 0:
        i += 1
        n = n / p
    return i


def has_divisor(q, factors):  # problem 5
    """Check whether q has a factor in factors."""
    divisor_found = False
    for f in factors:
        if q % f == 0:
            divisor_found = True
            break
    return divisor_found


def is_prime(q):
    """Check whether is a prime"""
    if q < 2:
        is_p = False
    else:
        is_p = True
        for f in range(2, int(np.sqrt(q)) + 1):
            if q % f == 0:
                is_p = False
                break
    return is_p


def prime_powers(n):  # problem 5
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
                if not has_divisor(q, p):
                    p[q] = divisor_power(q, n)
            q += 1
        # no factors means that n is a prime
        if len(p) == 0:
            p = {n: 1}
    return p


def distinct_prime_powers(n):  # problem 5
    """Simple distinct prime factor tracker."""
    p = []
    # primes are naturals greater than 2
    if n < 2:
        pass
    else:
        # test for factors
        q = 2
        while q <= n / 2:
            if n % q == 0:
                if not has_divisor(q, p):
                    p.append(q)
            q += 1
        # no factors means that n is a prime
        if len(p) == 0:
            p = [n]
    return p


def is_palindrome(n: str) -> bool:
    return n == n[::-1]


def search_largest_palindrome(n):  # problem 4
    best = 1
    for i in range(n + 1)[::-1]:
        for j in range(n + 1)[::-1]:
            if i * j <= best:
                pass
            elif is_palindrome(i * j):
                best = i * j
    return best


def divisor_sum(n: int) -> int:
    powers = prime_powers(n)
    s = 1
    for p in powers:
        s *= (p ** (powers[p] + 1) - 1) / (p - 1)
    d = s - n
    return int(d)


def n_divisors(n: int) -> int:
    powers = prime_powers(n)
    s = 1
    for p in powers:
        s *= (powers[p] + 1)
    d = s - 1
    return int(d)


def reduce_fraction(numerator: int, denominator: int) -> Tuple[int, int]:
    npp = prime_powers(numerator)
    dpp = prime_powers(denominator)

    n = 1
    d = 1

    all_primes = set(list(npp) + list(dpp))
    for p in all_primes:
        if (p in npp) and (p in dpp):
            n *= p ** max(0, npp[p] - dpp[p])
            d *= p ** max(0, dpp[p] - npp[p])
        elif p in npp:
            n *= p ** npp[p]
        else:
            d *= p ** dpp[p]

    return n, d


def triangle(n):
    return n * (n + 1) // 2


def pentagon(n):
    return n * (3 * n - 1) // 2


def hexagon(n):
    return n * (2 * n - 1)
