import argparse


def solution(n):
    """Another awkward situation where this is a 1-liner in Python"""
    s = sum([int(d) for d in str(2 ** n)])
    return s


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 16: Power Digit Sum')
    parser.add_argument('--n', type=int, default=1000)
    args = parser.parse_args()

    problem = 16
    n = args.n

    answer = solution(n)
    print(f'The answer to problem {problem} for n={n} is {answer}')
