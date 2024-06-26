import set_root
import argparse
from tqdm import tqdm
from src.library import gcd


def solution(m):
    """Not as pretty as 072 - can calculate reduced fractions less than 1/2 easily via symmetry
    But nothing obvious to get those less than 1/3 without a longer computation than brute forcing (1/3, 1/2).
    """

    c = -1  # adjust count upfront for (n, d) = (1, 2)
    for d in tqdm(range(2, m + 1)):
        for n in range(d // 3 + 1, d // 2 + 1):
            if gcd(n, d) == 1:
                c += 1

    return c


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 73: Counting Fractions in a Range')
    parser.add_argument('--n', type=int, default=12000)
    args = parser.parse_args()

    problem = 73
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
