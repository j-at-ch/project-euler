import argparse
import numpy as np
from typing import List


def find_triangle_numbers(n: int) -> List:
    """Find all triangle numbers up to n"""
    t = [int(i * (i + 1) / 2) for i in range(n)]
    return t


def encode_word(w):
    """Find 1-indexed ordinal for alphabet position."""
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = 0
    for letter in w.upper():
        s += alpha.index(letter) + 1
    return s


def solution(path):
    # read in the file.
    with open(path, 'r') as f:
        words = f.read()

    # clean up the punctuation and encode the words.
    words = words.replace('"', '').split(',')
    encoded_words = [encode_word(w) for w in words]

    # generate all the necessary triangle numbers
    max_triangle = int(np.sqrt(2 * max(encoded_words)))
    triangles = find_triangle_numbers(max_triangle)

    # count the number of triangles found in the word list.
    n = 0
    for w in encoded_words:
        if w in triangles:
            n += 1
    return n


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 42: Coded Triangle Numbers')
    parser.add_argument('--path', type=str, default='data/042.txt')
    args = parser.parse_args()

    problem = 42
    answer = solution(args.path)

    print(f'The answer to problem {problem} is {answer}')
