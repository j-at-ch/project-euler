import argparse
from itertools import permutations


def solution():
    """Semi analytical solution:
    It's easy to see that it's not possible to form a 9-digit number with seed 9x or 9xx.
    There's only one option for the seed 9 (given in the question). All that's left to explore is 9xxx.
    We know that 9xxx cannot multiply by 2 to 19xxx otherwise not a pandigital product.
    Hence must be 9 followed by {2, 3, 4}. Try 4. Then 94xx18[89]xx therefore cannot be pandigital.
    Search remaining...
    """
    digits = '765432'
    for p in permutations(digits, 3):
        base = f'9{p[0]}{p[1]}{p[2]}'
        prod = str(int(base)) + str(2 * int(base))
        if set(prod) == set('123456789'):
            return int(prod)
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 38: Pandigital Multiples')
    args = parser.parse_args()

    problem = 38
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
