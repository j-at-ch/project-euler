import argparse
from collections import Counter


def solution():
    """The strategy is to look for ascii space characters ' '. In natural language these should
    be the most numerous ascii characters. We'll count incidences of the spaces for each possible
    key, then select based on that with gives the max.
    """

    with open('data/059.txt') as f:
        text = [int(c) for c in f.read().split(',')]

    # we're told that the length-3 key is made up of lower case characters
    alphabet_range = [97, 123]

    corpora = []

    for ki in [0, 1, 2]:
        key_corpus = []
        for a in range(*alphabet_range):
            corpus = []
            for i, c in enumerate(text):
                if i % 3 == ki:
                    corpus.append(chr(c ^ a))
            key_corpus.append(Counter(corpus))
        corpora.append(key_corpus)

    keys = []
    for crpa in corpora:
        max_idx = None
        max_spaces = 0
        for i, corp in enumerate(crpa):
            n_spaces = corp.get(' ', 0)
            if n_spaces > max_spaces:
                max_idx = 97 + i
                max_spaces = n_spaces
        keys.append(max_idx)

    v = 0
    s = ''
    for i, c in enumerate(text):
        if i % 3 == 0:
            s += chr(c ^ keys[0])
            v += c ^ keys[0]
        elif i % 3 == 1:
            s += chr(c ^ keys[1])
            v += c ^ keys[1]
        elif i % 3 == 2:
            s += chr(c ^ keys[2])
            v += c ^ keys[2]
        else:
            pass
    return v


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 59: XOR Decryption')
    args = parser.parse_args()

    problem = 59
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
