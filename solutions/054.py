import argparse
from collections import Counter


def rank(hand):
    card_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    rank_order = [
        'high card', 'one pair',
        'two pairs', 'three of a kind',
        'straight', 'flush',
        'full house', 'four of a kind',
        'straight flush', 'royal flush'
    ]

    hand_ranks = {}

    values = [card_order.index(c[0]) for c in hand]
    suits = [c[1] for c in hand]

    sorted_values = sorted(values)

    counts = Counter(values)
    value_counts = Counter([c for v, c in counts.items()])

    if len(set(suits)) == 1:
        if sorted_values == [8, 9, 10, 11, 12]:
            hand_ranks['royal flush'] = [1]
        if len(set(sorted_values)) == 5 and sorted_values[-1] - sorted_values[0] == 4:
            hand_ranks['straight flush'] = [sorted_values[-1]]
        hand_ranks['flush'] = sorted_values[::-1]

    if 4 in value_counts:
        hand_ranks['four of a kind'] = [k for k, v in counts.items() if v == 4]

    if 2 in value_counts and 3 in value_counts:
        hand_ranks['full house'] = [[k for k, v in counts.items() if v == 3][0],
                                    [k for k, v in counts.items() if v == 2][0]]

    if len(set(sorted_values)) == 5 and sorted_values[-1] - sorted_values[0] == 4:
        hand_ranks['straight'] = [sorted_values[-1]]

    if 3 in value_counts:
        hand_ranks['three of a kind'] = [k for k, v in counts.items() if v == 3]

    if 2 in value_counts and value_counts[2] == 2:
        hand_ranks['two pairs'] = [k for k, v in counts.items() if v == 2][::-1]

    if 2 in value_counts:
        hand_ranks['one pair'] = [k for k, v in counts.items() if v == 2]

    hand_ranks['high card'] = [sorted_values[-1]]

    hand_name = sorted(hand_ranks, key=rank_order.index)[-1]
    hand_rank = rank_order.index(hand_name)

    return hand_rank, hand_ranks[hand_name], sorted_values[::-1]


def solution():
    """Horribly verbose code, but it works."""

    with open('data/054.txt', 'r') as f:
        data = f.read()

    games = [[r.split(' ')[0:5], r.split(' ')[5:]] for r in data.split('\n')]

    c = 0
    for g in games:
        a = rank(g[0])
        b = rank(g[1])

        w = None
        if a[0] > b[0]:
            w = 1
        elif a[0] < b[0]:
            w = 0
        else:
            pass

        if w is None:
            for z in zip(a[1], b[1]):
                if z[0] > z[1]:
                    w = 1
                    break
                elif z[0] < z[1]:
                    w = 0
                    break
                else:
                    pass

        if w is None:
            for z in zip(a[2], b[2]):
                if z[0] > z[1]:
                    w = 1
                    break
                elif z[0] < z[1]:
                    w = 0
                    break
                else:
                    pass

        c += w
    return c


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 54: Poker Hands')
    args = parser.parse_args()

    problem = 54
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
