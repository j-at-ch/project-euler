import set_root
import argparse
from src.library import fibonacci


def solution(n):
    """Get ordinal index of first fibonacci number with at least 1000 digits"""
    i = 1
    d = len(str(fibonacci(i)))

    while d < n:
        i += 1
        d = len(str(fibonacci(i)))
    return i


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 25: 1000-digit Fibonacci Number')
    parser.add_argument('--n', type=int, default=1000)
    args = parser.parse_args()

    problem = 25
    answer = solution(n=args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
