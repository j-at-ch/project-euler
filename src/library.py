from functools import cache
import numpy as np
from typing import Tuple


@cache
def factorial(n: int) -> int:
    return n * factorial(n-1) if n > 1 else 1


@cache
def sum_factorials(n: int) -> int:
    return factorial(n) + sum_factorials(n - 1) if n > 1 else 1


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
    if q <= 1:
        return False
    elif q < 4:
        return True
    elif q % 2 == 0:
        return False
    elif q < 9:
        return True
    elif q % 3 == 0:
        return False
    else:
        max_factor = int(np.sqrt(q))
        a = 5
        while a <= max_factor:
            if q % a == 0 or q % (a + 2) == 0:
                return False
            else:
                a += 6
        return True


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


def distinct_prime_powers(n):
    """Simple distinct prime factor tracker."""
    p = []
    k = n
    # primes are naturals greater than 2
    if n < 2:
        pass
    else:
        # test for factors
        q = 2
        while k > 1:
            is_factor = False
            power = 0
            while k % q == 0:
                k = k // q
                is_factor = True
                power += 1
            if is_factor:
                p.append(q)
            if q == 2:
                q += 1
            else:
                q += 2
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


def square(n):
    return n ** 2


def pentagon(n):
    return n * (3 * n - 1) // 2


def hexagon(n):
    return n * (2 * n - 1)


def heptagon(n):
    return n * (5 * n - 3) // 2


def octagon(n):
    return n * (3 * n - 2)


def surd_continued_fraction(s):
    """Find the continued fraction representation of sqrt(s)."""
    surd = np.sqrt(s)
    if surd - int(surd) == 0:
        return [int(surd)]

    rep = []
    a = int(np.sqrt(s))
    rep.append(a)

    m = 0
    d = 1
    while True:
        m = d * a - m
        d = (s - m ** 2) / d
        a = int((rep[0] + m) / d)
        rep.append(a)
        if a == 2 * rep[0]:
            break
    return rep


def totient(n):
    pp = distinct_prime_powers(n)
    t = n
    for p in pp:
        t *= p - 1
    for p in pp:
        t //= p
    return t


def gcd(a, b):
    """Find the greatest common divisor (hcf) of a and b using the Euclidean algorithm"""
    while True:
        if b > a:
            a, b = b, a
        a = a % b
        b = b
        if a == 0:
            return b


@cache
def partition(n):
    """From `Recurrences for the partition function and its relatives` by John A Ewell.
    This is the pentagonal recurrence relation proved by Euler.
    """
    if n < 0:
        return 0
    elif n < 2:
        return 1
    s = 0
    k_max = int((np.sqrt(24 * n + 1) + 1) / 6)
    for k in range(1, k_max + 1):
        s += (-1) ** (k - 1) * (
            partition(n - int((k * (3 * k - 1) / 2)))
            + partition(n - int((k * (3 * k + 1) / 2)))
        )
    return s
