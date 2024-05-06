import argparse
import numpy as np
from typing import List


def divisible_digit_triples(m: int) -> List:
    triples_list = []
    for i in range(0, int(1000 / m)):
        triple = f'{str(m * i):0>3}'
        n_unique = len(set(triple))
        if n_unique == 3:
            triples_list.append(triple)
    return triples_list


def solution():
    base_list = divisible_digit_triples(17)  # initiate from most highly constrained triples
    divisors = [13, 11, 7, 5, 3, 2, 1]  # list remaining divisors.

    for i, d in enumerate(divisors):
        running_list = []
        for bs in base_list:  # take base right-hand aligned substring
            for pr in divisible_digit_triples(d):  # attempt to left-match a new substring.
                if pr[1:] == bs[:2]:  # check digit overlap
                    if len(set(pr[0] + bs)) == i + 4:  # check the unique digit count of substring is correct
                        running_list.append(pr[0] + bs)
        base_list = running_list

    ans = sum([int(d) for d in base_list])
    return ans


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 43: Sub-string Divisibility')
    args = parser.parse_args()

    problem = 43
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
