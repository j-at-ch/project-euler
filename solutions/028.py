import argparse


def solution(n):
    assert n % 2 == 1
    s = 1
    for i in range(1, int((n + 1) / 2)):
        for j in range(2 * i - 1, 2 * i + 3):
            s += 2 * i * j + 1
    return s


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 28: Number Spiral Diagonals')
    parser.add_argument('--n', type=int, default=1001, help='The side-length of the square spiral. Must be odd!')
    args = parser.parse_args()

    problem = 28
    answer = solution(n=args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
