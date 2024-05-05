import set_root
import argparse
from library import has_divisor


def solution(n):
    prime_list = []
    i = 0
    q = 2
    while q < n:
        if q % 1000 == 0:
            print(q)
        if not has_divisor(q, prime_list):
            prime_list.append(q)
            i += 1
        q += 1
    return sum(prime_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 10: Summation of Primes')
    parser.add_argument('--n', type=int, default=10, help='Expects 17')
    args = parser.parse_args()

    n = args.n
    answer = solution(n)
    print(f'The answer for the PROBLEM n={args.n} is {answer}')
