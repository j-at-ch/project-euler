import set_root
import argparse
from tqdm import tqdm
from src.library import is_prime


def solution(n):
    """
    My new favourite: the first observation is that we just need to iterate through the denominators
    since the number of reduced fractions of denominator d is totient(d). The naive approach of calculating
    this afresh per d is too slow. The key observation then is that to calculate totient(d) we need only the distinct
    prime factors of d. We can therefore do the inverse of sieving: iterate through primes p and generate all their
    multiples in the range of interest p * k, appending these to a list for each of the elements in the target range.
    """

    # generate a placeholder array of distinct prime factors
    dp = dict(zip(range(2, n + 1), [[] for _ in range(2, n + 1)]))

    # add a prime to the relevant array members whenever multiples of the prime are < n
    for p in range(2, n + 1):
        if is_prime(p):
            k = 1
            while k * p < n + 1:
                dp[k * p] += [p]
                k += 1

    s = 0
    # iterate through denominators
    for d in tqdm(range(2, n + 1)):
        # calculate the totient by hand
        t = d
        for f in dp[d]:
            t = t // f * (f - 1)
        s += t

    return s


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 72: Counting Fractions')
    parser.add_argument('--n', type=int, default=10**6)
    args = parser.parse_args()

    problem = 72
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
