import argparse


def solution():
    # read data
    with open('data/067.txt', 'r') as f:
        arr = f.read().split('\n')[:-1][::-1]

    # build up the triangle
    triangle = []
    for row in arr:
        row = [int(d) for d in row.split(' ')]
        triangle.append(row)

    # iterate bottom-up, adding the max of children of each row to the parent.
    t = []
    i = 0
    while i < len(triangle) - 1:
        t0 = triangle[i]
        t = triangle[i + 1]
        for j in range(len(t)):
            t[j] += max(t0[j], t0[j + 1])
        i += 1
    return t[0]


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 67: Maximum Path Sum II')
    args = parser.parse_args()

    problem = 67
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
