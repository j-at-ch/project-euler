import argparse


def solution(n):
    d = 0
    for i in range(1, n + 1):
        d += i ** i % 10 ** 10
    d = f'{str(d)[-10:]:0>10}'
    return d


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 48: Self Powers')
    parser.add_argument('--n', type=int, default=10)
    args = parser.parse_args()

    problem = 48
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n = {args.n} is {answer}')
