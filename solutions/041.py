import set_root
import argparse
from itertools import permutations
from src.library import is_prime


def solution():
    for i in range(9, 0, -1):
        for p in permutations('987654321'[-i:]):
            q = int(''.join(p))
            if int(p[-1]) % 2 == 0:
                pass
            elif is_prime(q):
                return q
            else:
                pass
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 41: Digit Factorials')
    args = parser.parse_args()

    problem = 41
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
