import set_root
import argparse
from src.library import is_palindrome


def reverse_and_sum(n):
    n += int(str(n)[::-1])
    return n


def solution(n):
    l = 0
    p = []
    for i in range(n):
        if i in p:
            continue
        cond = True
        j = 0
        q = i
        while cond and j < 50:
            j += 1
            q = reverse_and_sum(q)
            if is_palindrome(str(q)):
                p.append(i)
                cond = False
        if cond:
            l += 1
    return l


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 55: Lychrel Numbers')
    parser.add_argument('--n', type=int, default=10000)
    args = parser.parse_args()

    problem = 55
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
