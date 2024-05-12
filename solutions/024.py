import set_root
import argparse
from typing import List
from src.library import factorial


def solution(p, n) -> List:
    """Find the p-th lexicographic permutation of n!

    :param p: Zero-is-first index for the position of the permutation to select
    :param n: Number of digits used in the permutation
    :return: The p-th lexicographic permutation of n!
    """
    init = [i for i in range(n)]
    w = []
    for i in range(1, n + 1):
        f = factorial(n - i)
        w.append(init.pop(p // f))
        p = p - (p // f) * f
    return w


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 24: Lexicographic Permutations')
    parser.add_argument('--n', type=int, default=10)
    parser.add_argument('--p', type=int, default=10**6)
    args = parser.parse_args()

    problem = 24
    answer = solution(p=args.p - 1, n=args.n)  # switch from ordinal to zero-is-first

    print(f'The answer to problem {problem} for n={args.n} and p={args.p} is {answer}')
