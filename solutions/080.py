import set_root
import argparse
import numpy as np
from src.library import surd_continued_fraction


def solution(n):
    s = 0
    frac_list = {}
    for i in range(1, n + 1):
        sqrt = np.sqrt(i)
        if sqrt - int(sqrt) == 0:
            continue
        else:
            cfr = surd_continued_fraction(i)
            pp = cfr[1:]
            n_list = [0, 1, cfr[0]]
            d_list = [1, 0, 1]

            j = 0
            while True:
                n_list.append(pp[j % len(pp)] * n_list[-1] + n_list[-2])
                d_list.append(pp[j % len(pp)] * d_list[-1] + d_list[-2])
                j += 1
                max_approx_err = d_list[-2] * d_list[-1]
                # continued fraction approximations are good to 1 / (d_n * d_{n+1})
                if len(str(max_approx_err)) > 101:
                    break

            n = n_list[-2]
            d = d_list[-2]
            a_list = []
            j = 0
            while j < 101:
                a = n // d
                a_list.append(a)
                n = 10 * (n - a * d)
                j += 1

            frac_list[i] = a_list
            s += sum(a_list[0:100])
    return s


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 80: Square Root Digital Expansion')
    parser.add_argument('--n', type=int, default=100)
    args = parser.parse_args()

    problem = 80
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
