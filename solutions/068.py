import argparse
from itertools import permutations, combinations


def solution(n):
    # read data
    solutions = []

    nodes = range(1, 2 * n)
    idx_str = ''.join([f'{i}{n + i}{n + ((i + 1) % n)}' for i in range(n)])

    # Force 10 to be an outside node and select other outside nodes.
    combs = [c + (10,) for c in combinations(nodes, 4)]
    for c in combs:

        # only permute the part of the combination which is not the least external node.
        for c1 in permutations(c[1:]):
            c2 = (c[0],) + c1

            # permute the remaining numbers
            for d in permutations(set(nodes) - set(c2)):
                p = c2 + d

                # form the magic n-gon list from the chosen nodes
                ngon = [p[int(i)] for i in idx_str]

                # run through ngon arms checking the sum
                i = 1
                a = sum(ngon[0:3])
                while i < 5 and sum(ngon[3 * i: 3 * (i + 1)]) == a:
                    i += 1

                # if all tests pass, append to solutions
                if i == 5:
                    solutions.append(''.join([str(i) for i in ngon]))

    return max(solutions)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 68: Magic 5-gon Ring')
    parser.add_argument('--n', type=int, default=5)
    args = parser.parse_args()

    problem = 68
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
