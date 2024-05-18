import set_root
import argparse
import time
from src.library import reduce_fraction


def solution():
    """Reduce search space by analysis - then implement a reduce fraction function"""
    num = 1
    den = 1

    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):

                if 10 * a * c - 9 * b * c - a * b == 0:
                    s = [a, b, c]
                    if len(set(s)) != 1 and a <= c:
                        num *= a * b
                        den *= c * a

                if 10 * a * b - 9 * a * c - b * c == 0:
                    s = [a, b, c]
                    if len(set(s)) != 1 and a <= c:
                        num *= a * b
                        den *= b * c

    _, reduced_den = reduce_fraction(num, den)
    return reduced_den


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 33: Digit Cancelling Fractions')
    args = parser.parse_args()

    problem = 33
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
