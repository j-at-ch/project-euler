import set_root
import argparse
import numpy as np
from library import factorial
from tqdm import tqdm


def factorial_digit_sum(n: int) -> int:
    ds = 0
    for s in str(n):
        ds += factorial(int(s))
    return ds


def bound_search_space():
    """Both LHS and RHS are strictly increasing. Find the first breakage."""
    bound_holds = True
    n = 1
    while bound_holds:
        n += 1
        lhs = (n - 1) * np.log(10)
        rhs = np.log(n) + np.log(4 * 10 ** 5)
        bound_holds = lhs < rhs
    return n - 1


def solution(n):
    """Only search within bounds."""
    lower = 10
    curious = 0
    for i in tqdm(range(lower, n)):
        fds = factorial_digit_sum(i)
        if i == fds:
            curious += fds
    return curious


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 34: Digit Factorials')
    parser.add_argument('--n', type=int, default=10**6, help='Search range for n.')
    args = parser.parse_args()

    problem = 34
    n = bound_search_space()
    answer = solution(10**n)

    print(f'The answer to problem {problem} with n = {10**n} is {answer}')
