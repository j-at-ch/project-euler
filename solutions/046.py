import set_root
import argparse
import numpy as np
from src.library import is_prime


def solution():

    p = set()
    i = 1
    m_prev = 2
    cond = True

    while cond:
        m_curr = (2 * i + 1) ** 2

        for q in range(m_prev, m_curr + 1):
            if is_prime(q):
                p.add(q)

        for j in range(1, i + 1):
            q = (2 * i + 1) * (2 * j + 1)
            t = set(q - 2 * k ** 2 for k in range(1, int(np.sqrt(q // 2)) + 1))
            if len(t.intersection(p)) == 0:
                print('*' * 10 + '>', q)
                print(q, p, t)
                cond = False
        i += 1
        m_prev = m_curr
    return q


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 46: Goldbach')
    parser.add_argument('--t', type=int, default=60)
    args = parser.parse_args()

    problem = 46
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
