import argparse


def solution():
    """
    DP to the rescue! Needs some improvement, but the idea is to sweep from L2R checking up and down paths as
    for 082, then sweep R2L up and down, and iterate to convergence.
    """
    with open('data/083.txt') as f:
        arr = [[int(a) for a in r.split(',')] for r in f.read().strip('\n').split('\n')]

    m = len(arr)
    n = len(arr[0])
    dp = [[float('inf')] * (n + 2) for _ in range(m + 2)]

    dp_prev = None
    while dp != dp_prev:
        dp_prev = [r[:] for r in dp]
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                path_part = 0 if i * j == 1 else min(dp[i - 1][j], dp[i][j - 1])
                dp[i][j] = min(dp[i][j], arr[i - 1][j - 1] + path_part)

            for i in range(m, 0, -1):
                dp[i][j] = min(dp[i][j], arr[i - 1][j - 1] + min(dp[i + 1][j], dp[i][j + 1]))

        for j in range(m, 0, -1):
            for i in range(1, m + 1):
                dp[i][j] = min(dp[i][j], arr[i - 1][j - 1] + min(dp[i + 1][j], dp[i][j + 1]))

    return dp[m][n]


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 83: Path Sum: Four Ways')
    args = parser.parse_args()

    problem = 83
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
