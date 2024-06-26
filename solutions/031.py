import argparse


def solution(denominations, n):
    """Bottom-up dynamic programming approach"""
    s = [0 for k in range(n + 1)]
    s[0] = 1
    for d in denominations:
        for j in range(d, n + 1):
            s[j] += s[j - d]
    return s[n]


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 31: Coin Sums')
    parser.add_argument('--n', type=int, default=200)
    args = parser.parse_args()

    problem = 31
    denominations = [1, 2, 5, 10, 20, 50, 100, 200]
    answer = solution(denominations, args.n)

    print(f'The answer to problem {problem} with denominations={denominations} for n={args.n} is {answer}')
