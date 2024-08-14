import argparse
import set_root
import numpy as np
from collections import Counter
from tqdm import tqdm
from src.library import is_prime


def solution(N):
    numbers = [i for i in range(1, N + 1)]
    divisor_powers = {i: {} for i in numbers}

    primes = []
    for i in tqdm(range(N)):
        if is_prime(i):
            primes.append(i)

    for p in tqdm(primes):
        for r in range(1, int(np.log(N) / np.log(p)) + 1):
            for k in range(1, N // (p ** r) + 1):
                if r == 1:
                    divisor_powers[k * p ** r][p] = 1
                else:
                    divisor_powers[k * p ** r][p] += 1

    divisor_sums = {i: 0 for i in numbers}

    for d in divisor_powers:
        dp = divisor_powers[d]
        s = 1
        for p in dp:
            s *= (p ** (dp[p] + 1) - 1) / (p - 1)
        ds = s - d
        divisor_sums[d] = int(ds)

    chains = {}
    len_longest_chain = 0

    s = 0
    for i in tqdm(range(2, N)):
        chain = [i]
        c = i
        while True:
            c = divisor_sums[c]
            if c < i:
                break
            elif c in chain:
                for j in chain:
                    chains[j] = i
                if len(chain) > len_longest_chain:
                    len_longest_chain = len(chain)
                break
            elif c > N:
                break
            else:
                chain.append(c)

    answer = Counter(chains.values()).most_common(n=1)[0][0]
    return answer


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 88: Roman Numerals')
    parser.add_argument('--N', type=int, default=10**6, required=False)
    args = parser.parse_args()

    problem = 88
    answer = solution(args.N)

    print(f'The answer to problem {problem} for n={args.N} is {answer}')
