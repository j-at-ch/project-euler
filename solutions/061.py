import set_root
import argparse
import numpy as np
from tqdm import tqdm
from itertools import permutations
from src.library import triangle, square, pentagon, hexagon, heptagon, octagon


def real_quadratic_roots(a, b, c):
    roots = []
    if b ** 2 - 4 * a * c < 0:
        pass
    else:
        roots.append((- b + np.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
        roots.append((- b - np.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    return roots


def solution(n=4):
    """Find exactly the 4-digit figurate numbers necessary.
    Permute, then iterate them, checking the relevant overlap conditions.
    """

    triangles = []
    r0 = int(real_quadratic_roots(1 / 2, 1 / 2, -10 ** (n - 1))[0]) + 1
    r1 = int(real_quadratic_roots(1 / 2, 1 / 2, -10 ** n)[0])
    for i in range(r0, r1):
        f = triangle(i)
        triangles.append(f)

    squares = []
    r0 = int(real_quadratic_roots(1, 0, -10 ** (n - 1))[0]) + 1
    r1 = int(real_quadratic_roots(1, 0, -10 ** n)[0])
    for i in range(r0, r1):
        f = square(i)
        squares.append(f)

    pentagons = []
    r0 = int(real_quadratic_roots(3 / 2, -1 / 2, -10 ** (n - 1))[0]) + 1
    r1 = int(real_quadratic_roots(3 / 2, -1 / 2, -10 ** n)[0])
    for i in range(r0, r1):
        f = pentagon(i)
        pentagons.append(f)

    hexagons = []
    r0 = int(real_quadratic_roots(2, -1, -10 ** (n - 1))[0]) + 1
    r1 = int(real_quadratic_roots(2, -1, -10 ** n)[0])
    for i in range(r0, r1):
        f = hexagon(i)
        hexagons.append(f)

    heptagons = []
    r0 = int(real_quadratic_roots(5 / 2, -3 / 2, -10 ** (n - 1))[0]) + 1
    r1 = int(real_quadratic_roots(5 / 2, -3 / 2, -10 ** n)[0])
    for i in range(r0, r1):
        f = heptagon(i)
        heptagons.append(f)

    octagons = []
    r0 = int(real_quadratic_roots(3, -2, -10 ** (n - 1))[0]) + 1
    r1 = int(real_quadratic_roots(3, -2, -10 ** n)[0])
    for i in range(r0, r1):
        f = octagon(i)
        octagons.append(f)

    collections = [
        squares,
        pentagons,
        hexagons,
        heptagons,
        octagons
    ]

    sol = None
    for perm in tqdm(permutations(collections), total=120):
        for t in triangles:
            for s in perm[0]:
                if str(t)[2:] != str(s)[0:2]:
                    continue
                for p in perm[1]:
                    if str(s)[2:] != str(p)[0:2]:
                        continue
                    for h in perm[2]:
                        if str(p)[2:] != str(h)[0:2]:
                            continue
                        for k in perm[3]:
                            if str(h)[2:] != str(k)[0:2]:
                                continue
                            for o in perm[4]:
                                if str(k)[2:] != str(o)[0:2]:
                                    continue
                                if str(o)[2:] != str(t)[0:2]:
                                    continue
                                sol = [t, s, p, h, k, o]

    return sum(sol)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 61: Cyclical Figurate Numbers')
    parser.add_argument('--n', type=int, default=4)
    args = parser.parse_args()

    problem = 61
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
