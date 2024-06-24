import argparse
import numpy as np


def solution(n):
    """
    My favourite problem so far... Goes from O(n**3) to stoppable O(n**2) with some clever counting.
    The shortest route is always c**2 + (a + b)**2 for a given cuboid (a, b, c) where a <= b <= c. By
    iterating over c in the outside loop, then d = a + b on the inner, we can stop as soon as a solution is found.
    """
    result = None
    k = 0
    c = 0
    while result is None:
        c += 1
        for d in range(2, 2 * c + 1):
            s = np.sqrt(c ** 2 + d ** 2)
            if s - int(s) == 0:
                k += d // 2 - max(d - c - 1, 0)
            if k > n:
                result = c
                break
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 86: Cuboid Route')
    parser.add_argument('--n', type=int, default=10**6)
    args = parser.parse_args()

    problem = 86
    answer = solution(args.n)

    print(f'The answer to problem {problem} is {answer}')
