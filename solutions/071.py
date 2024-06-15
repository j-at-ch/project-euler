import set_root
import argparse
import numpy as np
from tqdm import tqdm
from src.library import gcd


def solution(m, verbose=True):
    """
    Search a specific range, skipping non-reduced fractions and breaking once a difference smaller
    than the current minimum can no longer be achieved with denominators of size
    less than or equal the current.
    """

    D_max = m
    D_min = 7 * 10 ** 5 - 1

    min_diff = np.inf
    min_n = None
    min_d = None
    # roam denominators in reverse order up to D_min (obvious solution with 299999 / 700000)
    for d in tqdm(range(D_max, D_min, -1)):
        # roam numerators
        for n in range(d * 3 // 7, 1, -1):
            # we'll find these later on
            if gcd(d, n) > 1:
                continue

            # if this holds, then it's not possible to find a smaller diff with the remaining range of d.
            if 1 / (7 * d) > min_diff:
                break

            # check the distance to 3 / 7
            diff = (3 * d - 7 * n) / (7 * d)
            if diff < min_diff:
                min_diff = diff
                min_n = n
                min_d = d

    if verbose:
        print(min_n, min_d, min_diff)
    return min_n


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 71: Ordered Fractions')
    parser.add_argument('--n', type=int, default=10**6)
    args = parser.parse_args()

    problem = 71
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
