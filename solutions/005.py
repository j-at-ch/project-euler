import argparse


def divisor_power(p, n):
    i = 0
    while n % p == 0:
        i += 1
        n = n / p
    return i


def known_divisor(q, factors):
    is_known = True
    for f in factors:
        if q % f == 0:
            is_known = False
    return is_known


def prime_factors(n):
    """Simple distinct prime factor tracker"""
    p = {}
    # primes are naturals greater than 2
    if n < 2:
        pass
    else:
        # test for factors
        q = 2
        while q <= n / 2:
            if n % q == 0:
                if known_divisor(q, p):
                    p[q] = divisor_power(q, n)
            q += 1
        # no factors means that n is a prime
        if len(p) == 0:
            p = {n: 1}
    return p


def solution(n):
    """Keep a dictionary of the greatest power of a prime factor
    amongst naturals >= n.
    """
    d = {}
    for m in range(1, n + 1):
        p_m = prime_factors(m)
        for p in p_m:
            if p_m[p] > d.get(p, 0):
                d[p] = p_m[p]
    out = 1
    for k in d:
        out *= k**d[k]
    return out


def test(m, n):
    is_pass = True
    for i in range(1, n + 1):
        if m % i != 0:
            is_pass = False
    return is_pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=10, help='Default value expects 2520')
    args = parser.parse_args()

    n = args.n
    answer = solution(n)

    print(f'Is pass? {test(answer, n)}')
    print(f'The answer for the PROBLEM n={args.n} is {answer}')
