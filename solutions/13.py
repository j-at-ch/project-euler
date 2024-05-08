import set_root
import argparse


def solution(n):
    """Maybe this was difficult at time of writing? [shrug]"""
    with open('data/0013.txt', 'r') as f:
        numbers = [int(n) for n in f.read().split('\n')]
    s = sum(numbers)
    first_n_digits = str(s)[0:n]
    return first_n_digits


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 13: Large Sum')
    parser.add_argument('--n', type=int, default=10)
    args = parser.parse_args()

    problem = 13
    n = args.n

    answer = solution(n)
    print(f'The answer to problem {problem} for n={n} is {answer}')
