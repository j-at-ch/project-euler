import set_root
import argparse
import numpy as np
from src.library import is_prime


def solution(n):
    # gather all of the necessary primes
    primes = []
    for q in range(2, int(np.sqrt(n)) + 1):
        if is_prime(q):
            primes.append(q)

    # gather all of the necessary squares, cubes and quartics upfront
    squares = []
    cubes = []
    quartics = []
    for p in primes:
        if p ** 2 < n:
            squares.append(p ** 2)
        if p ** 3 < n:
            cubes.append(p ** 3)
        if p ** 4 < n:
            quartics.append(p ** 4)

    # There shouldn't be too many to search for n ~ 10**7. Brute force the O(n**3)
    solutions = []
    for s in squares:
        for c in cubes:
            for q in quartics:
                triple_sum = s + c + q
                if triple_sum < n:
                    solutions.append(triple_sum)

    result = len(set(solutions))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 87: Prime Power Triples')
    parser.add_argument('--n', type=int, default=50*10**6)
    args = parser.parse_args()

    problem = 87
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
