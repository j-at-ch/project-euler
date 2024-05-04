import argparse


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def search_largest_palindrome(n):
    best = 1
    for i in range(n + 1)[::-1]:
        for j in range(n + 1)[::-1]:
            if i * j <= best:
                pass
            elif is_palindrome(i * j):
                best = i * j
    return best


def solution(n):
    return search_largest_palindrome(10**n)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=3)
    args = parser.parse_args()

    print(f'The answer for n={args.n} is {solution(args.n)}')
