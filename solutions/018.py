import argparse
from typing import List


def find_max_path(triangle: List[List[int]]) -> int:
    """Pass.
    :param triangle: Top-heavy representation of the number triangle.
    :return: The sum of the maximum path's values.
    """
    t = triangle
    for i in range(len(t) - 1):
        for j in range(len(t[i + 1])):
            t[i + 1][j] += max(t[i][j], t[i][j + 1])
    return t[-1][0]


def solution():
    # read data
    with open('data/018.txt', 'r') as f:
        arr = f.read()

    # parse data into reverse list-of-lists structure
    triangle = []
    for ar in arr.split('\n')[::-1]:
        tr = []
        for s in ar.split(' '):
            tr.append(int(s))
        triangle.append(tr)

    # get max path
    out = find_max_path(triangle)
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 18: Maximum Path Sum I')
    args = parser.parse_args()

    problem = 18

    answer = solution()
    print(f'The answer to problem {problem} is {answer}')
