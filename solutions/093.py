import argparse
from tqdm import tqdm
from itertools import product, permutations


digits = []
for a in range(1, 10):
    for b in range(a + 1, 10):
        for c in range(b + 1, 10):
            for d in range(c + 1, 10):
                digits.append((a, b, c, d))

operations = list(product(['+', '/', '-', '*'], repeat=3))

brackets = [
    '( {a} {o1} {b} ) {o2} {c} {o3} {d}',
    '  {a} {o1} ( {b} {o2} {c} ) {o3} {d}',
    '  {a} {o1} {b} {o2} ( {c} {o3} {d} )',
    '( {a} {o1} {b} ) {o2} ( {c} {o3} {d} )',
    '(( {a} {o1} {b} ) {o2} {c} ) {o3} {d}',
    '( {a} {o1} ( {b} {o2} {c} )) {o3} {d}',
    ' {a} {o1} (( {b} {o2} {c} ) {o3} {d} )',
    ' {a} {o1} ( {b} {o2} ( {c} {o3} {d} ))'
]


def compute_expression(digits, operations, bracket):
    kwargs = dict(
        zip(
            ['a', 'b', 'c', 'd', 'o1', 'o2', 'o3'],
            digits + operations
        )
    )
    expr = bracket.format(**kwargs)
    try:
        ans = eval(expr)
    except ZeroDivisionError:
        ans = -1
    return ans


def solution():
    """Simple exhaustive search - just requires a bit of thought represent expressions"""
    m = 100  # maximum search (guess)
    best_minimum = 0
    best_digs = None

    for digs in tqdm(digits):
        outs = []
        for dig in permutations(digs):
            for ops in operations:
                for bracket in brackets:
                    out = compute_expression(dig, ops, bracket)
                    if (out > 0) and (out - int(out) == 0):
                        outs.append(int(out))
        outs = set(outs)

        min_missing = min(set(range(1, m)) - outs)
        if min_missing > best_minimum:
            best_minimum = min_missing
            best_digs = digs

    return ''.join(map(str, best_digs))


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 93: Arithmetic Expressions')
    args = parser.parse_args()

    problem = 93
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
