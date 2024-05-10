import argparse


base_increments = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_increments = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def check_leap(n: int) -> bool:
    return (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)


def solution():
    """Count month-starts with day_n % 7 = 0"""
    count = 0
    day_n = 366

    if 366 % 7 == 0:
        count += 1

    for y in range(1901, 2001):
        incr = leap_increments if check_leap(y) else base_increments
        for i in range(12):
            day_n += incr[i]
            if day_n % 7 == 0:
                count += 1

    return count


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 19: Counting Sundays')
    args = parser.parse_args()

    problem = 19

    answer = solution()
    print(f'The answer to problem {problem} is {answer}')
