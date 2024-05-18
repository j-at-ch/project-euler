import set_root
import argparse
from src.library import is_palindrome


def solution(n):
    s = []
    for i in range(n):
        if is_palindrome(str(i)) and is_palindrome(str(bin(i)[2:])):
            s.append(i)
    return sum(s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 36: Double-base Palindromes')
    parser.add_argument('--n', type=int, default=10**6)
    args = parser.parse_args()

    problem = 36
    answer = solution(args.n)

    print(f'The answer to problem {problem} with n={args.n} is {answer}')
