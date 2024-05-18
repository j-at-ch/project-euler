import argparse
from itertools import permutations
from tqdm import tqdm
import time


def solution(t=60):
    tic = time.time()

    solutions = []
    perms = permutations(range(1, 10))
    for i in tqdm(perms):
        for e in range(5, 8):
            for m in range(1, e - 1):
                k = list(str(d) for d in i)
                a = int(''.join(k[0:m]))
                b = int(''.join(k[m:e]))
                c = int(''.join(k[e:]))
                if a * b == c:
                    solutions.append(c)
        if time.time() - tic > t:
            raise RuntimeError('Time is out!')

    return sum(set(solutions))


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 32: Pandigital Products')
    args = parser.parse_args()

    problem = 32
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
