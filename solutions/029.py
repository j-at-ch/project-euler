import argparse


def solution(n):
    """Brute force should be enough for this one."""
    s = set(a ** b for a in range(2, n + 1) for b in range(2, n + 1))
    return len(s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 29: Distinct Powers')
    parser.add_argument('--n', type=int, default=100)
    args = parser.parse_args()

    problem = 29
    answer = solution(n=args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
