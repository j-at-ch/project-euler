import argparse


def encode_word(w) -> int:
    """Find word's alphabetical value."""
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = 0
    for letter in w.upper():
        s += alpha.index(letter) + 1
    return s


def solution():
    # read data and tidy to a list
    with open('data/022.txt', 'r') as f:
        words = f.read().replace('"', '').split(',')

    # sort words
    sorted_words = sorted(words)

    # sum up the position-weighted values
    s = 0
    for i, w in enumerate(sorted_words):
        s += (i + 1) * encode_word(w)
    return s


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 22: Names Scores')
    args = parser.parse_args()

    problem = 22

    answer = solution()
    print(f'The answer to problem {problem} is {answer}')
