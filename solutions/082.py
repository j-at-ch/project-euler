import argparse


def solution():
    """Finally! This one took some thinking. The idea is to propagate maxima column by column."""
    with open('data/082.txt') as f:
        arr = [[int(a) for a in r.split(',')] for r in f.read().strip('\n').split('\n')]

    m = len(arr)
    n = len(arr[0])

    dp = [[float('inf')] * (n + 2) for _ in range(m + 2)]

    for i in range(1, m + 1):
        dp[i][1] = arr[i - 1][0]

    for j in range(2, n + 1):
        for i in range(1, m + 1):
            dp[i][j] = arr[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])

        for i in range(m, 0, -1):
            dp[i][j] = min(dp[i][j], arr[i - 1][j - 1] + min(dp[i + 1][j], dp[i][j + 1]))

    return int(min([dp[i][m] for i in range(m + 1)]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 82: Path Sum: Three Ways')
    args = parser.parse_args()

    problem = 82
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
