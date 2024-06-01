import argparse
import time
import numpy as np


def pentagon(n):
    return n * (3 * n - 1) // 2


def solution(t=60):
    """Note - this solution does not have an appropriate stopping condition.
    The solution remains a guess in the context of the 1-minute timeout.
    """
    tic = time.time()
    best = np.inf
    m = 1
    pentagons = set()
    lower = 1
    c = tic
    while True:
        # add pentagons between prev n and 2Pn + 3n + 1
        upper = int((1 + np.sqrt(1 + 12 * (4 * pentagon(m) + 6 * m + 2))) // 6)

        a = time.time() - c
        for i in range(lower + 1, upper + 1):
            p = pentagon(i)
            pentagons.add(p)

        b = time.time() - a
        for i in range(1, m)[::-1]:
            pa = pentagon(m) + pentagon(i)
            pd = pentagon(m) - pentagon(i)
            if pa in pentagons:
                if pd in pentagons:
                    if pd < best:
                        best = pd
                        print(m, i, pa, pd)
        c = time.time() - b
        m += 1

        if 3 * m - 2 > best:
            break

        toc = time.time() - tic
        if toc > t:
            print("Timeout!")
            print(best, 3 * m - 2)
            break
        lower = upper
    return best


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 44: Pentagon Numbers')
    parser.add_argument('--t', type=int, default=60)
    args = parser.parse_args()

    problem = 44
    answer = solution(args.t)

    print(f'The answer to problem {problem} is {answer}')
