import argparse
import numpy as np


def solution():
    p = [0] * 1001
    b = 1
    while b < 1000 // 2:
        for a in range(1, b + 1):
            c = np.sqrt(a ** 2 + b ** 2)
            if c - c // 1 == 0:
                i = int(a + b + c)
                if i <= 1000:
                    p[i] += 1
        b += 1
    return p.index(max(p))


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 39: Integer Right Triangles')
    args = parser.parse_args()

    problem = 39
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
