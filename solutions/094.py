import argparse


def solution(n):
    """Pattern spotting: there is a recursive pattern. [Still need to prove it holds]."""
    i = [-2, 1, 3]
    a = [1, 8]
    b = [1, 2]
    d = -1

    perim = 6 * i[-1] + 2 * d
    total = 4 + perim

    while True:
        i = a[-1] + b[-1] - b[-2] + d
        a.append(3 * i - d)
        b.append(i - d)
        perim = 6 * i + 2 * d
        d *= -1
        if perim <= n:
            total += perim
        else:
            break
    return total


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 94: Almost Equilateral Triangles')
    parser.add_argument('--n', type=int, default=10**9)
    args = parser.parse_args()

    problem = 94
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
