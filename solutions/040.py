import argparse


def solution(n):
    s = 1
    l = 0
    k = 0
    for i in range(1, n):
        l_prev = l
        l += len(str(i))
        if l >= 10 ** k:
            s *= int(str(i)[10 ** k - l_prev - 1])
            k += 1
    return s


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Problem 40: Champernowne's Constant")
    parser.add_argument('--n', default=10**5, type=int)
    args = parser.parse_args()

    problem = 40
    answer = solution(args.n)

    print(f'The answer to problem {problem} is {answer}')
