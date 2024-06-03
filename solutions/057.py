import argparse


def solution(n):
    c = 0
    num = 3
    den = 2
    for i in range(1, n):
        num_prev = num
        den_prev = den
        den = den_prev + num_prev
        num = 2 * den_prev + num_prev
        if len(str(num)) > len(str(den)):
            c += 1
    return c


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 57: Square Root Convergents')
    parser.add_argument('--n', type=int, default=1000)
    args = parser.parse_args()

    problem = 57
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
