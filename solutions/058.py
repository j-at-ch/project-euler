import set_root
import argparse
from src.library import is_prime


def solution(thr):
    p = 0
    i = 1
    l = 0
    r = 1
    while r > thr:
        i += 4
        l += 1
        d = [(2 * l + 1) ** 2 + a * l for a in [-6, -4, -2, 0]]
        for q in d:
            if is_prime(q):
                p += 1
        r = p / i
    return 2 * l + 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 58: Spiral Primes')
    parser.add_argument('--thr', type=float, default=0.1)
    args = parser.parse_args()

    problem = 58
    answer = solution(args.thr)

    print(f'The answer to problem {problem} for thr={args.thr} is {answer}')
