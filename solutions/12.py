import set_root
import argparse
from src.library import n_divisors


def triangle_number(n):
    return n * (n + 1) // 2


def solution(n):
    """Make use of super-cool property that n and n + 1 must be coprime
    and therefore cannot share divisors. Find the number of divisors of n and n + 1
    for t = n * (n + 1) // 2 separately, take their product (corrected for exclusion of t).
    """
    d = 0
    t = 0
    i = 1
    while d < n:
        t = triangle_number(i)
        if i % 2 == 0:
            d1 = n_divisors(i // 2)
            d2 = n_divisors(i + 1)
        else:
            d1 = n_divisors(i)
            d2 = n_divisors((i + 1) // 2)
        d = (d1 + 1) * (d2 + 1) - 1
        i += 1
    return t


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 12: Highly Divisible Triangular Number')
    parser.add_argument('--n', type=int, default=500)
    args = parser.parse_args()

    problem = 12
    n = args.n

    answer = solution(n)
    print(f'The answer to problem {problem} for n={n} is {answer}')
