import set_root
import argparse
from src.library import factorial


def solution(n):
    """There's an elegant solution to this problem.
    Let d be the symbol for a down move and r be the symbol for a right move.
    Then each path is uniquely encoded by a word consisting of n * 'd' and n * 'r'.
    There is a natural unique ordering, so we don't need to consider permutations -
    the solution is 2n choose n.
    """
    return factorial(2 * n) // (factorial(n)**2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 15: Lattice Paths')
    parser.add_argument('--n', type=int, default=20)
    args = parser.parse_args()

    problem = 15
    n = args.n

    answer = solution(n)
    print(f'The answer to problem {problem} for n={n} is {answer}')
