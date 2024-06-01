import set_root
import argparse
from src.library import is_prime
from tqdm import tqdm


def solution(n):
    # get all primes in range upfront.
    pp = []
    for i in range(2, n):
        if is_prime(i):
            pp.append(i)

    pb = 2
    lb = 0
    for i in tqdm(range(len(pp))):
        for j in range(i, len(pp)):
            l = j + 1 - i

            # 2 is the only even prime
            if i > 0 and l % 2 == 0:
                continue

            # continue if len of summands cannot be best
            if l <= lb:
                continue

            q = sum(list(pp)[i:j + 1])

            # if q is out of range break all subsequent sums.
            if q > n:
                break

            if is_prime(q):
                if j + 1 - i > lb:
                    pb = q
                    lb = j + 1 - i
    return pb


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 50: Consecutive Prime Sum')
    parser.add_argument('--n', type=int, default=10 ** 6)
    args = parser.parse_args()

    problem = 50
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
