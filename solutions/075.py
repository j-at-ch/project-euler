import set_root
import argparse
from collections import Counter
from tqdm import tqdm
from src.library import gcd


def pyth_trip(m, n):
    return (m ** 2 - n ** 2), 2 * m * n, (m ** 2 + n ** 2)


def solution(max_len):
    perimeters = []
    for m in tqdm(range(2, max_len)):
        for n in range(1, min(m, max_len // m)):
            if (n >= m) or (gcd(m, n) > 1) or (m % 2 == n % 2):
                continue
            else:
                pr = sum(pyth_trip(m, n))
                perimeters += ([l for l in range(pr, max_len, pr)])

    sol = Counter(Counter(perimeters).values())[1]
    return sol


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 75: Singular Integer Right Triangles')
    parser.add_argument('--l', type=int, default=1500000)
    args = parser.parse_args()

    problem = 75
    answer = solution(args.l)

    print(f'The answer to problem {problem} for l={args.l} is {answer}')
