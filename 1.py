import argparse
import numpy as np


def arithmetic_sum(n: int) -> int:
    return int(0.5 * n * (n + 1))


def solution(n):
    """
    Use inclusion exclusion together with the exact formula for arithmetic sums.
    """
    m = n - 1  # The question asks for less than n.
    s_3 = 3 * arithmetic_sum(np.floor(m / 3))
    s_5 = 5 * arithmetic_sum(np.floor(m / 5))
    s_15 = 15 * arithmetic_sum(np.floor(m / 15))
    return s_3 + s_5 - s_15


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=1000)
    args = parser.parse_args()

    print(f'The answer for n={args.n} is {solution(args.n)}')
