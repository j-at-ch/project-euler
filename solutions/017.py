import argparse
from functools import cache


l0 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
l1 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
l2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


@cache
def int_to_str(m):
    if 1 <= m <= 10:
        out = l0[m - 1]
    elif 10 < m < 20:
        out = l1[m - 11]
    elif 20 <= m < 100:
        if m % 10 == 0:
            out = l2[(m - 20) // 10]
        else:
            out = '-'.join([l2[(m - 20) // 10], int_to_str(m % 10)])
    elif 100 <= m < 1000:
        if m % 100 == 0:
            out = ' '.join([l0[m // 100 - 1], 'hundred'])
        else:
            out = ' '.join([l0[m // 100 - 1], 'hundred', 'and', int_to_str(m % 100)])
    elif m == 1000:
        out = 'one thousand'
    else:
        out = ''
    return out


def solution(n):
    s = 0
    for i in range(1, n + 1):
        cleaned_str = int_to_str(i).replace(' ', '').replace('-', '')
        s += len(cleaned_str)
    return s


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 17: ')
    parser.add_argument('--n', type=int, default=1000)
    args = parser.parse_args()

    problem = 17
    n = args.n

    answer = solution(n)
    print(f'The answer to problem {problem} for n={n} is {answer}')
