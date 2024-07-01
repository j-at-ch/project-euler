import argparse


def solution(n):
    """The naive solution, solving quadratic and generating solutions wasn't rapid enough.
    I ended up pattern spotting the recursive relations in r and b. I assume there's something
    deeper going on here to do with CFRs, but I haven't found it yet.
    """
    rlst = [0, 1, 6]
    blst = [1, 3]
    while rlst[-1] + blst[-1] < n:
        r = 6 * rlst[-1] - rlst[-2]
        b = 6 * blst[-1] - blst[-2] - 2
        rlst.append(r)
        blst.append(b)
    return blst[-1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 100: Arranged Probability')
    parser.add_argument('--n', type=int, default=10**12)
    args = parser.parse_args()

    problem = 100
    answer = solution(args.n)

    print(f'The answer to problem {problem} for n={args.n} is {answer}')
