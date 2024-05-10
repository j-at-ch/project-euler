import set_root
import argparse
from src.library import factorial


def solution(n):
    """Again... Too easy in Python."""
    digits = str(factorial(n))
    s = 0
    for d in digits:
        s += int(d)
    return s


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 20: Factorial Digit Sum')
    parser.add_argument('--n', type=int, default=100)
    args = parser.parse_args()

    problem = 20
    n = args.n

    answer = solution(n)
    print(f'The answer to problem {problem} for n={n} is {answer}')
