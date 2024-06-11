import set_root
import argparse
from src.library import surd_continued_fraction


def solution(n):
    """This scf function includes the first convergent, so look for even length reps."""
    k = 0
    for i in range(1, 10000):
        if len(surd_continued_fraction(i)) % 2 == 0:
            k += 1
    return k


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 64: Odd Period Square Roots')
    parser.add_argument('--n', type=int, default=10000)
    args = parser.parse_args()

    problem = 64
    answer = solution(args.n)

    print(f'The answer to problem {problem} is {answer}')
