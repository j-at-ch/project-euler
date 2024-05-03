import argparse
from functools import cache


@cache
def fib(m):
    """Fibonacci numbers for m >=1 with fib(1)=1 and fib(2) = 2."""
    return fib(m - 1) + fib(m - 2) if m > 2 else m


def solution(n):
    """
    Sum even Fibonacci numbers using the fact that even numbers
    can only occur as fib(m) for m % 3 = 2 (by construction).
    """
    s = 0
    i = 1
    m = 0
    while m < n:
        m = fib(i)
        if i % 3 == 2:
            s += m
        i += 1
    return s


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=4_000_000)
    args = parser.parse_args()

    print(f'The answer for n={args.n} is {solution(args.n)}')
