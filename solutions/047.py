import set_root
import argparse
import time
from src.library import distinct_prime_powers2


def solution(n, t):
    start = time.time()

    s = None
    i = 4
    k = 0

    while True:
        d = len(distinct_prime_powers2(i))
        if d == n:
            k += 1
        elif d != n:
            k = 0

        if k == n:
            s = i - n + 1
            break
        i += 1

        if time.time() - start > t:
            print('Timeout!')
            break
    return s


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 47: Distinct Primes Factors')
    parser.add_argument('--n', type=int, default=4)
    parser.add_argument('--t', type=int, default=60)
    args = parser.parse_args()

    problem = 47
    answer = solution(args.n, args.t)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
