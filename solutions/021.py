import set_root
import argparse
from tqdm import tqdm
from src.library import divisor_sum


def divisor_path(m, stop_if=lambda x: (x == 1) or (x > 1000)):
    p = [m]
    d = divisor_sum(m)
    while (d not in p) and not stop_if(d):
        p.append(d)
        d = divisor_sum(d)
    p.append(d)
    return p


def solution(n):
    amicable = set()
    terminal = set()
    for i in tqdm(range(2, n+1)):
        if i in amicable or i in terminal:
            continue
        p = divisor_path(i, stop_if=lambda x: (x == 1) or (x > n))
        if p[0] == p[-1] and len(p) == 3:
            amicable = amicable.union(set(p[0:-1]))
        elif p[-1] == 1:
            terminal = terminal.union(set(p[0:-1]))
    return sum(amicable)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 21: Amicable Numbers')
    parser.add_argument('--n', type=int, default=10000)
    args = parser.parse_args()

    problem = 21
    n = args.n

    answer = solution(n)
    print(f'The answer to problem {problem} for n={n} is {answer}')
