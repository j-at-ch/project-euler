import argparse


def solution(n):
    s = []
    l = []
    for i in range(1, n):
        for j in range(1, n):
            p = 0
            for k in str(i ** j):
                p += int(k)
            s.append(p)
            l.append((i, j))
    return max(s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 56: Powerful Digit Sum')
    parser.add_argument('--n', type=int, default=100)
    args = parser.parse_args()

    problem = 56
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
