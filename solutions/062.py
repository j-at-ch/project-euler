import set_root
import argparse
import numpy as np
from collections import Counter


def solution(n):
    """Iterate through k-digit cubes and accumulate sorted string representations of them.
    Break once a k for which there is a rep of frequency n is found.
    """

    k = 4
    while True:
        p0 = int(np.power(10 ** (k - 1), 1 / 3)) + 1
        p1 = int(np.power(10 ** k, 1 / 3))

        cube_to_string = {}
        cube_strings = []
        for i in range(p0, p1):
            cstr = ''.join(sorted(str(i ** 3)))
            cube_strings.append(cstr)
            cube_to_string[i ** 3] = cstr

        counts = Counter(cube_strings).most_common()
        if len(counts) > 0 and counts[0][1] == n:
            break
        k += 1

    sol = min([c for c, v in cube_to_string.items() if v == counts[0][0]])

    return sol


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 62: Cubic Permutations')
    parser.add_argument('--n', type=int, default=5)
    args = parser.parse_args()

    problem = 62
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
