import argparse
import numpy as np
from tqdm import tqdm


def count_rectangles(w, h):
    return h * (h + 1) * w * (w + 1) // 4


def solution(n):
    """
    Use an analytic solution to count the number of rectangles - simple product-sum rearrangement.
    Then prune the search space.
    """
    W = 2 * 10 ** 6
    area = None
    min_dist = np.inf
    for w in tqdm(range(1, W)):
        for h in range(w, int(W / w)):
            n_rect = count_rectangles(w, h)
            dist = n - n_rect if n > n_rect else n_rect - n
            if dist < min_dist:
                min_dist = dist
                area = w * h
    return area


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 85: Counting Rectangles')
    parser.add_argument('--n', type=int, default=2 * 10**6)
    args = parser.parse_args()

    problem = 85
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
