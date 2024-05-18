import set_root
import argparse
from src.library import is_prime


def solution(n):
    s = []  # track solutions
    i = 0  # track current solution count
    j = 23
    while i < n:
        if is_prime(j):
            q = str(j)
            is_pass = True
            # attempt to refute prime truncatability
            for k in range(1, len(q)):
                if is_prime(int(q[k:])) and is_prime(int(q[:k])):
                    pass
                else:
                    is_pass = False
                    break
            # if j passes all tests, append to solutions.
            if is_pass:
                s.append(j)
                i += 1
        # iterate j by 2 no even primes > 2
        j += 2
    return sum(s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 37: Truncatable Primes')
    parser.add_argument('--n', type=int, default=11)
    args = parser.parse_args()

    problem = 37
    answer = solution(args.n)

    print(f'The answer to problem {problem} with n={args.n} is {answer}')
