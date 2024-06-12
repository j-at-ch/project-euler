import set_root
import argparse
from tqdm import tqdm
from src.library import surd_continued_fraction


def solution(n, verbose=False):
    """
    Test convergents until a solution to Pell's equation is found.
    """
    d_max = 1
    x_max = 0

    for d in tqdm(range(2, n)):
        cfr = surd_continued_fraction(d)
        if len(cfr) > 1:
            periodic = cfr[1:]
            xs = [0, 1, cfr[0]]
            ys = [1, 0, 1]

            j = 0
            while True:
                xs.append(periodic[j % len(periodic)] * xs[-1] + xs[-2])
                ys.append(periodic[j % len(periodic)] * ys[-1] + ys[-2])
                pell = xs[-1] ** 2 - d * ys[-1] ** 2
                if pell == 1:
                    if verbose:
                        print(f'{xs[-1] ** 2} - {d} * {ys[-1] ** 2} = {pell}')
                    break
                if xs[-1] > x_max:
                    x_max = xs[-1]
                    d_max = d
                j += 1
    return d_max


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 66: Diophantine Equation')
    parser.add_argument('--n', type=int, default=1000)
    args = parser.parse_args()

    problem = 66
    answer = solution(args.n)

    print(f'The answer to problem {problem} is {answer}')
