import argparse
from tqdm import tqdm
from itertools import combinations


def check_edges(d1, d2):
    conditions = [
        (1 in d1 and 8 in d2) or (1 in d2 and 8 in d1),
        (2 in d1 and 5 in d2) or (2 in d2 and 5 in d1),
        (0 in d1 and 1 in d2) or (0 in d2 and 1 in d1),
        (0 in d1 and 4 in d2) or (0 in d2 and 4 in d1),
        (0 in d1 and (6 in d2 or 9 in d2)) or (0 in d2 and (6 in d1 or 9 in d1)),
        (1 in d1 and (6 in d2 or 9 in d2)) or (1 in d2 and (6 in d1 or 9 in d1)),
        (3 in d1 and (6 in d2 or 9 in d2)) or (3 in d2 and (6 in d1 or 9 in d1)),
        (4 in d1 and (6 in d2 or 9 in d2)) or (4 in d2 and (6 in d1 or 9 in d1))
    ]
    return all(conditions)


def solution():
    """Embarrassingly easy in Python. Thought I might need to generate bipartite graphs,
    but the combinatorics are so small, that brute search-and-test is rapid."""

    dice = [c for c in combinations(range(0, 10), 6)]

    total = 0
    for i in tqdm(range(len(dice))):
        for j in range(i, len(dice)):
            if check_edges(dice[i], dice[j]):
                total += 1

    return total


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 90: Cube Digit Pairs')
    args = parser.parse_args()

    problem = 90
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
