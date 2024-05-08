import argparse


def solution(n):
    d = {}
    for a in range(0, int(n / 3)):
        for b in range(a + 1, int((n - a) / 2)):
            c = n - a - b
            if a ** 2 + b ** 2 == c ** 2:
                d['triple'] = (a, b, c)
                d['product'] = a * b * c
    return d


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 9: Special Pythagorean Triplet')
    parser.add_argument('--n', type=int, default=1000)
    args = parser.parse_args()

    n = args.n
    answer = solution(n)
    print(f'The answer for the PROBLEM n={args.n} is {answer["product"]}')
