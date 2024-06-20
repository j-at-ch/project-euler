import argparse


def solution():
    with open('data/081.txt') as f:
        rows = [r.split(',') for r in f.read().strip('\n').split('\n')]
        arr = [[int(a) for a in r] for r in rows]

    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if i == 0 and j == 0:
                pass
            elif i == 0 and j > 0:
                arr[0][j] += arr[0][j - 1]
                arr[j][0] += arr[j - 1][0]
            elif i > 0 and i == j:
                arr[i][i] += min(arr[i][i - 1], arr[i - 1][i])
            else:
                arr[i][j] += min(arr[i][j - 1], arr[i - 1][j])
                arr[j][i] += min(arr[j - 1][i], arr[j][i - 1])
    return arr[-1][-1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 81: Path Sum: Two Ways')
    args = parser.parse_args()

    problem = 81
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
