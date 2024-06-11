import set_root
import argparse


def solution(n):
    """
    Use the recursion relation for numerator of the convergents given
    the continued fraction representation.
    """

    numerators = [0, 1]
    k = 1
    for i in range(n):
        if i == 0:
            a = 2
        elif i % 3 != 2:
            a = 1
        else:
            a = 2 * k
            k += 1
        numerators.append(a * numerators[-1] + numerators[-2])
    sol = sum([int(d) for d in str(numerators[-1])])
    return sol


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 65: Convergents of e')
    parser.add_argument('--n', type=int, default=100)
    args = parser.parse_args()

    problem = 65
    answer = solution(args.n)

    print(f'The answer to problem {problem} is {answer}')
