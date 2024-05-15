import set_root
import argparse
import numpy as np
from src.library import is_prime


def solution(n):
    """Simple search for the longest sequence produced by a quadratic."""
    max_seq_len = 0
    prod_ab = 0
    for b in range(2, n + 1):
        if is_prime(b):
            for a in range(-n, n + 1):
                i = 0
                while True:
                    q = i ** 2 + a * i + b
                    if q <= 1:
                        break
                    if is_prime(q):
                        i += 1
                    else:
                        break
                if i > max_seq_len:
                    max_seq_len = i
                    prod_ab = a * b
    return prod_ab


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 27: Quadratic Primes')
    parser.add_argument('--n', type=int, default=1000)
    args = parser.parse_args()

    problem = 27
    answer = solution(n=args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
