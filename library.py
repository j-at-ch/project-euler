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
