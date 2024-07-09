import argparse
from tqdm import tqdm


def solution(n):
    """Fairly brute force, but uses the Pythagoras's Theorem to guarantee RATs."""
    t = 0
    for x0 in tqdm(range(n + 1)):

        for y0 in range(n + 1):
            if x0 == y0 == 0:  # (0, 0) forms a degenerate triangle.
                continue

            for x1 in range(n + 1):
                for y1 in range(n + 1):
                    if x1 == y1 == 0:  # (0, 0) forms a degenerate triangle.
                        continue

                    if y1 * x0 > y0 * x1:  # to achieve distinct enumeration.
                        pass
                    else:
                        continue

                    triple = sorted([
                        x0 ** 2 + y0 ** 2,
                        x1 ** 2 + y1 ** 2,
                        (x1 - x0) ** 2 + (y1 - y0) ** 2
                    ])

                    if triple[0] + triple[1] == triple[2]:
                        t += 1
    return t


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 91: Right Triangles with Integer Coordinates')
    parser.add_argument('--n', type=int, default=50)
    args = parser.parse_args()

    problem = 91
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}.')
