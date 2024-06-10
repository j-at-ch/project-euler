import set_root
import argparse
from src.library import is_prime
from tqdm import tqdm
import numpy as np


def solution(m):
    """Set a target space of primes, collate edges, then apply recursive set intersections to find
    prime sets of sufficient size.
    """

    primes = []
    for i in range(2, m):
        if is_prime(i):
            primes.append(i)

    pairs = {}
    for i in tqdm(range(len(primes))):
        pairs[primes[i]] = []
        for j in range(i, len(primes)):
            if is_prime(int(str(primes[i]) + str(primes[j]))) and is_prime(int(str(primes[j]) + str(primes[i]))):
                pairs[primes[i]].append(primes[j])

    solutions = []
    for p1 in pairs:
        s1 = set(pairs[p1])
        if len(pairs[p1]) == 0:
            continue
        for p2 in pairs[p1]:
            s2 = s1.intersection(set(pairs[p2]))
            if len(s2) == 0:
                continue
            for p3 in s2:
                s3 = s2.intersection(set(pairs[p3]))
                if len(s3) == 0:
                    continue
                for p4 in s3:
                    s4 = s3.intersection(set(pairs[p4]))
                    if len(s4) == 0:
                        continue
                    for p5 in s4:
                        s5 = s4.intersection(set(pairs[p5]))
                        if len(s5) == 0:
                            solutions.append([p1, p2, p3, p4, p5])

    out = 5*m
    for s in solutions:
        if sum(s) < out:
            out = sum(s)

    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 60: Prime Pair Sets')
    parser.add_argument('--m', type=int, default=10**4)
    args = parser.parse_args()

    problem = 60
    answer = solution(args.m)

    print(f'The answer to problem {problem} is {answer}')
