#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # base case if n = 0, return 0

    if n == 2:
        return eating_cookies(n-2) + eating_cookies(n-1)
    elif n == 1:
        return eating_cookies(n-1)
    elif n == 0:
        return 1
    else:
        return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)

    # cycle through actions and subtract n by each action
    # once not divisible by 3, divide by 2, etc, then subtract 1 until 0
    # increment counter
    # return counter


print(eating_cookies(10))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
