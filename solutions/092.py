import argparse
from tqdm import tqdm


def solution(n):
    """Simple hash map solution."""
    hsh = {}
    for i in tqdm(range(1, n)):
        k = i
        chain = [k]
        while True:
            if k not in hsh:
                chain.append(k)
                k = sum([int(d) ** 2 for d in str(k)])
                if k == 1 or k == 89:
                    c = [1, 89].index(k)
                    break
            else:
                c = hsh[k]
                break
        for j in chain:
            hsh[j] = c

    s = 0
    for h in hsh:
        s += hsh[h]
    return s


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 92: Square Digit Chains')
    parser.add_argument('--n', type=int, default=10**7)
    args = parser.parse_args()

    problem = 92
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
