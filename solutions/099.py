import argparse
import numpy as np


def solution():
    """Was expecting numpy to fail here, but we had just enough precision."""
    with open('data/099.txt') as f:
        arr = [[int(i) for i in row] for row in [row.split(',') for row in f.read().strip('\n').split('\n')]]

    log_arr = [arr[i][1] * np.log(arr[i][0]) for i in range(len(arr))]
    line_number = log_arr.index(max(log_arr)) + 1
    return line_number


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 99: Largest Exponential')
    args = parser.parse_args()

    problem = 99
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
