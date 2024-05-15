import argparse


def solution(n):
    """Another brute over a slightly refined range"""
    nth_powers = []
    for i in range(2, n * 9 ** n + 1):
        digits = str(i)
        ps = sum(int(d) ** n for d in digits)
        if i == ps:
            nth_powers.append(i)
    return sum(nth_powers)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 30: Digit Fifth Powers')
    parser.add_argument('--n', type=int, default=5)
    args = parser.parse_args()

    problem = 30
    answer = solution(n=args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
