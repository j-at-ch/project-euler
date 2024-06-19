import set_root
import argparse
from src.library import factorial
from tqdm import tqdm


def solution(n):
    # cache single digit factorials
    f = [factorial(i) for i in range(10)]

    solutions = []
    chains = {}
    for i in tqdm(range(n)):
        r = i
        l = [i]
        while True:
            s = sum(f[int(d)] for d in str(r))
            if s not in l:
                l.append(s)
                r = s
            else:
                if len(l) == 60:
                    solutions.append(i)
                break
        chains[i] = l
    return len(solutions)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 74: Digit Factorial Chains')
    parser.add_argument('--n', type=int, default=10**6)
    args = parser.parse_args()

    problem = 74
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
