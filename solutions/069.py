import set_root
import argparse
import numpy as np
from src.library import is_prime


def solution(n):
    """The n/totient(n) ratio is maximised by accumulating the product of small primes"""
    # get primes
    primes = []
    for q in range(2, int(np.sqrt(n))):
        if is_prime(q):
            primes.append(q)

    # build the composite maximiser
    i = 0
    m = 1
    while m < n / primes[i]:
        m *= primes[i]
        i += 1
    return m


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 69: Totient Maximum')
    parser.add_argument('--n', type=int, default=10**6)
    args = parser.parse_args()

    problem = 69
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
