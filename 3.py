import argparse
import numpy as np


def prime_factors(n):
    """Simple distinct prime factor tracker"""
    p = []
    q = 2
    while q <= np.sqrt(n):
        if n % q == 0:
            is_prime = True
            for f in p:
                if q % f == 0:
                    is_prime = False
            if is_prime:
                p.append(q)
        q += 1
    return p


def solution(n):
    pfs = prime_factors(n)
    return max(pfs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=600851475143)
    args = parser.parse_args()

    print(f'The answer for the n=13195 is {solution(13195)}')
    print(f'The answer for the n={args.n} is {solution(args.n)}')
