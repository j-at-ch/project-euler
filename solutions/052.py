import set_root
import argparse
from collections import Counter


def solution(n):
    sol = None
    k = 1
    i = 10 ** k
    cond1 = True

    while cond1:
        cond2 = True
        d = Counter(list(str(i)))
        j = 1
        while cond2:
            if Counter(list(str(j * i))) == d:
                j += 1
            else:
                cond2 = False
            if j > n:
                sol = i
                cond2 = False
                cond1 = False
        i += 1
        if str(i)[0] != '1':
            k += 1
            i = 10 ** k
    return sol


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 52: Permuted Multiples')
    parser.add_argument('--n', type=int, default=6)
    args = parser.parse_args()

    problem = 52
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
