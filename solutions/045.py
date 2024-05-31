import argparse
import numpy as np


def triangle(n):
    return n * (n + 1) // 2


def pentagon(n):
    return n * (3 * n - 1) // 2


def hexagon(n):
    return n * (2 * n - 1)


def solution(p_start):
    p = p_start
    while True:
        s = np.sqrt(1 + 4 * (3 * p ** 2 - p))
        if s - s // 1 == 0:
            h = (1 + s // 1) / 4
            if h == h // 1:
                out = [int(h), p]
                break
        p += 1
    return hexagon(out[0])


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 45: Triangular, Pentagonal and Hexagonal')
    parser.add_argument('--start', type=int, default=166)
    args = parser.parse_args()

    problem = 45
    answer = solution(args.start)

    print(f'The answer to problem {problem} is {answer}')
