import set_root
import argparse
from collections import Counter
from src.library import is_prime


def solution(n):
    q = 1001
    p = []
    for i in range(10 ** (n - 1) + 1, 10 ** n):
        if is_prime(i):
            p.append(i)

    triples = []
    while q < 10 ** n:
        d = 2
        while q + 2 * d < 10 ** n:
            if (q in p) and (q + d in p) and (q + 2 * d in p):
                c = Counter(list(str(q)))
                if Counter(list(str(q + d))) == c and Counter(list(str(q + 2 * d))) == c:
                    triples.append([q, q + d, q + 2 * d])
                d += 2
            else:
                d += 2
        q += 2

    out = None
    for tri in triples:
        if 1487 in tri and 4817 in tri and 8147 in tri:
            pass
        else:
            out = ''.join([str(t) for t in tri])
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 49: Prime Permutations')
    parser.add_argument('--n', type=int, default=4)
    args = parser.parse_args()

    problem = 49
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
