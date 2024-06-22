import argparse


def solution(n):
    """Super simple - just track the last 10 digits."""
    p = 7830457
    s = 28433
    i = 0
    while i < p:
        s = (s * 2) % (10 ** n)
        i += 1
    s += 1
    return s


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 97: Large Non-Mersenne Prime')
    parser.add_argument('--n', type=int, default=10, help='Number of final digits to track.')
    args = parser.parse_args()

    problem = 97
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
