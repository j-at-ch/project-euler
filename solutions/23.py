from tqdm import tqdm
import argparse
from src.library import divisor_sum


def find_abundants(n):
    abundants = []
    for i in tqdm(range(1, n + 1)):
        if divisor_sum(i) > i:
            abundants.append(i)
    return abundants


def solution():
    """"""
    upper = 28123
    abundants = find_abundants(28112)
    s = set()
    for a in abundants:
        for b in abundants:
            if b > upper - a:
                pass
            else:
                s.add(a + b)
    non_abundant_sums = set(range(1, upper + 1)) - s
    return sum(non_abundant_sums)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 23: Non-Abundant Sums')
    parser.add_argument('--n', type=int, default=None, help='Has no effect')
    args = parser.parse_args()

    problem = 23
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
