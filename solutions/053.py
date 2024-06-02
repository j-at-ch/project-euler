import set_root
import argparse
from src.library import factorial


def solution(n):
    c = 0
    for i in range(1, n + 1):
        for j in range(1, i):
            if int(factorial(i) / factorial(j) / factorial(i - j)) > 10 ** 6:
                c += 1
    return c


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 53: Combinatoric Selections')
    parser.add_argument('--n', type=int, default=100)
    args = parser.parse_args()

    problem = 53
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
