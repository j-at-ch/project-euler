import argparse
from src.library import has_divisor


def solution(n):
    """Only need to test *primes* up to the sqrt of each number until the desired n is reached."""
    prime_list = []
    i = 0
    q = 2
    while i < n:
        if not has_divisor(q, prime_list):
            prime_list.append(q)
            i += 1
        q += 1
    return prime_list[-1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=6, help='Default value expects 13')
    args = parser.parse_args()

    n = args.n
    answer = solution(n)
    print(f'The answer for the PROBLEM n={args.n} is {answer}')
