import set_root
import argparse
from src.library import is_prime
from tqdm import tqdm


def solution(n):
    """Find all primes, then conduct an accelerated search for circulars,
    skipping any prime containing a digit which cannot form
    a prime when in the rightmost position.
    """
    primes = []
    i = 2
    while i < 10 ** 6:
        if is_prime(i):
            primes.append(i)
        i += 1

    circular = []
    for p in tqdm(primes):
        q = str(p)
        if len(q) > 2:
            if ('2' in q) or ('4' in q) or ('5' in q) or ('6' in q) or ('8' in q) or ('0' in q):
                continue
        i = 0
        while i < len(q):
            q = q[-1] + q[0:-1]
            if int(q) in primes:
                i += 1
            else:
                break
        if i == len(q):
            circular.append(p)

    return len(circular)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 35: Circular Primes')
    parser.add_argument('--n', type=int, default=10**6)
    args = parser.parse_args()

    problem = 35
    answer = solution(args.n)

    print(f'The answer to problem {problem} with n = {args.n} is {answer}')
