import argparse
import numpy as np


def solution():
    """Finally! This one took some thinking. The idea is to propagate maxima column by column."""
    with open('data/082.txt') as f:
        arr = [[int(a) for a in r.split(',')] for r in f.read().strip('\n').split('\n')]

    n_rows = len(arr)
    n_cols = len(arr[0])

    arr = np.array(arr)
    dp = np.zeros_like(arr, dtype=float)
    dp[:, 0] = arr[:, 0]

    for j in range(1, n_cols):
        for i in range(n_rows):
            tmp_ij = np.inf
            for k in range(n_rows):
                if i < k:
                    idx_st = i + 1
                    idx_end = k + 1
                elif i > k:
                    idx_st = k
                    idx_end = i
                else:
                    idx_st = idx_end = k
                path_sum = dp[k, j - 1] + arr[idx_st:idx_end, j].sum()
                tmp_ij = min(tmp_ij, path_sum)
            dp[i, j] = arr[i, j] + tmp_ij

    return int(min(dp[:, -1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 82: Path Sum: Three Ways')
    args = parser.parse_args()

    problem = 82
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
