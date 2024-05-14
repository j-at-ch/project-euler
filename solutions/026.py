import set_root
import argparse
import numpy as np
from src.library import factorial


def solution(n):
    """Get ordinal index of first fibonacci number with at least 1000 digits"""
    denom = 1
    max_period = 0
    for i in range(2, n + 1):

        r_list = []
        r_prev = 1
        while True:
            p = np.ceil(np.log10(i / r_prev))
            a = (r_prev * 10 ** p) // i
            r = (r_prev * 10 ** p) - a * i

            r_prev = r
            if r_prev in r_list:
                r_list.append(r_prev)
                break

            r_list.append(r_prev)
            if r == 0:
                break

        period = len(r_list) - r_list.index(r) - 1

        if period > max_period:
            max_period = period
            denom = i

    return denom


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 26: Reciprocal Cycles')
    parser.add_argument('--n', type=int, default=1000)
    args = parser.parse_args()

    problem = 26
    answer = solution(n=args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
