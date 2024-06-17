import set_root
import argparse
from src.library import is_prime


def solution(n):
    """DP coin representation problem with a generous set of primes as the denominations."""

    primes = []
    for q in range(n):
        if is_prime(q):
            primes.append(q)

    s = [0] * n
    s[0] = 1
    sufficient_d = 0

    for d in primes:
        for j in range(d, n):
            s[j] += s[j - d]

        if max(s[0:d]) > 5000:
            sufficient_d = d
            break

    out = None
    for i, q in enumerate(s[0: sufficient_d]):
        if q > 5000:
            out = i
            break

    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 77: Prime Summations')
    parser.add_argument('--n', type=int, default=10**3)
    args = parser.parse_args()

    problem = 77
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
