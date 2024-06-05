import argparse


def solution():
    n = 0
    # base cannot be >= 10 otherwise trivially fails
    for a in range(1, 10):
        b = 1
        # for all bases < 10, at some point a ** b and a ** (b + 1) must have the same number of digits
        while len(str(a ** b)) == b:
            n += 1
            b += 1
    return n


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 63: Powerful Digit Counts')
    args = parser.parse_args()

    problem = 63
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
