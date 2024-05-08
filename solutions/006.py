import argparse


def solution(n):
    """Easy to work out an analytic solution via series cancellation.
    """
    square_of_sum = int(n * (n + 1) / 2) ** 2
    sum_of_square = int(n * (n + 1) * (2 * n + 1) / 6)
    return square_of_sum - sum_of_square


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=10, help='Default value expects 2640')
    args = parser.parse_args()

    n = args.n
    answer = solution(n)
    print(f'The answer for the PROBLEM n={args.n} is {answer}')
