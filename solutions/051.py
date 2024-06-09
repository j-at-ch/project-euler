import set_root
import argparse
from src.library import is_prime
from tqdm import tqdm


def solution(n):
    m = 1
    sol = []
    pos = {}

    while len(sol) == 0:
        print(f'Testing {m}-digit primes...')
        primes = []
        for i in range(10 ** (m - 1), 10 ** m):
            if is_prime(i):
                primes.append(i)

        for p in tqdm(primes):
            ps = list(int(d) for d in str(p))
            if min(ps) > 9 - n:
                pass
            else:
                for d in range(0, 10 - n):
                    k = 0
                    k_list = []
                    if d in ps:
                        i = d
                        while i < 10:
                            q = str(p).replace(str(d), str(i))
                            if is_prime(int(q)):
                                k += 1
                                i += 1
                                k_list.append(int(q))
                            else:
                                i += 1
                    pos[p] = k_list
                    if k == n:
                        sol.append(p)
            if len(sol) > 0:
                break
        m += 1
    return min(sol)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 51: Prime Digit Replacements')
    parser.add_argument('--n', type=int, default=8)
    args = parser.parse_args()

    problem = 51
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
