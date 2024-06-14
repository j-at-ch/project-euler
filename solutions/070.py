import set_root
import argparse
import numpy as np
from tqdm import tqdm
from collections import Counter
from src.library import is_prime


def solution():
    """
    The n/totient(n) ratio should be minimised by large primes. However...
    A prime is never a permutation of the digits of its totient, because totient(p) = p - 1.
    The next best thing is to look for products of a large primes as can be managed - these should be near
    to the sqrt of the maximum of the range n. Get primes in this range, then search triangle of products
    using the simple form for a product of two primes (p - 1) * (q - 1).
    """

    # get primes
    primes = []
    for p in tqdm(range(2, 10**4)):
        if is_prime(p):
            primes.append(p)

    # set up minimum totient ratio and minimum p * q
    min_r = np.inf
    min_pq = None
    for p in tqdm(primes[::-1]):
        for q in primes[0:primes.index(p) + 1][::-1]:
            # product
            pq = p * q
            if pq >= 10 ** 7:
                continue
            # totient
            tt = (p - 1) * (q - 1)
            if Counter(str(pq)) == Counter(str(tt)):
                r = pq / tt
                if r < min_r:
                    min_pq = pq
                    min_r = r
    return min_pq


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 70: Totient Permutation')
    parser.add_argument('--n', type=int, default=10**7)
    args = parser.parse_args()

    problem = 70
    answer = solution()

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
