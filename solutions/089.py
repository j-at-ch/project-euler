import set_root
import argparse
import numpy as np
from src.library import is_prime


def numeral2int(n):
    standards = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    specials = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    total = 0
    for s in specials:
        if s in n:
            total += specials[s]
            n = n.replace(s, '')

    total += sum([standards[s] for s in n])

    return total


def numeral_coefficients(a, d):
    if d == 1:
        c = ['I', 'V', 'X']
    elif d == 10:
        c = ['X', 'L', 'C']
    elif d == 100:
        c = ['C', 'D', 'M']
    else:
        raise ValueError('Unknown denomination `d`.')

    if a <= 3:
        return c[0] * a
    elif a == 4:
        return c[0] + c[1]
    elif a in [5, 6, 7, 8]:
        return c[1] + (a - 5) * c[0]
    elif a == 9:
        return c[0] + c[2]
    else:
        raise ValueError('Value of `a` out of range.')


def int2numeral(n):
    a_m = n // 1000
    r_m = n % 1000
    a_c = r_m // 100
    r_c = r_m % 100
    a_x = r_c // 10
    r_x = r_c % 10
    s = (
        a_m * 'M' +
        numeral_coefficients(a_c, 100) +
        numeral_coefficients(a_x, 10) +
        numeral_coefficients(r_x, 1)
    )
    return s


def solution():
    with open('data/089.txt', 'r') as f:
        numerals = f.read().split('\n')

    t = 0
    for m in numerals:
        t += len(m) - len(int2numeral(numeral2int(m)))

    return t


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 89: Roman Numerals')
    args = parser.parse_args()

    problem = 89
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
