import set_root
import argparse
from src.library import partition


def solution(n):
    """Use Euler's pentagonal recurrence relation for the partition function."""
    i = 0
    while partition(i) % n != 0:
        i += 1
    return i


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 78: Coin Partitions')
    parser.add_argument('--n', type=int, default=10**6)
    args = parser.parse_args()

    problem = 78
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
