import argparse


def solution(n):
    """DP coin representation problem with all integers as the set of denominations."""
    m = [0] * (n + 1)
    m[0] = 1
    for d in range(1, n + 1):
        for i in range(d, n + 1):
            m[i] += m[i - d]
    # exclude the singleton representation, n.
    return m[n] - 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 76: Counting Summations')
    parser.add_argument('--n', type=int, default=100)
    args = parser.parse_args()

    problem = 76
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
