import set_root
import argparse
from tqdm import tqdm
from functools import cache


@cache
def collatz_len(n):
    if n == 1:
        out = 1
    elif n % 2 == 0:
        out = 1 + collatz_len(n // 2)
    else:
        out = 1 + collatz_len(3 * n + 1)
    return out


def solution(n):
    m = 1
    l = 1
    for i in tqdm(range(2, n)):
        c = collatz_len(i)
        if c > l:
            m = i
            l = c
    return m


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 14: Longest Collatz Sequence')
    parser.add_argument('--n', type=int, default=10**6)
    args = parser.parse_args()

    problem = 14
    n = args.n

    answer = solution(n)
    print(f'The answer to problem {problem} for n={n} is {answer}')
