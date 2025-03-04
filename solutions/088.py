import argparse
import set_root
import numpy as np


def solution(N):
    answer = 'Too good to share... Sorry!'
    return answer


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 88: Product-sum numbers')
    parser.add_argument('--n', type=int, default=12000, required=False)
    args = parser.parse_args()

    problem = 88
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
