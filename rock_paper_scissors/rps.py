#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    plays = []

    def plays_rps(num, playlist=[]):
        if num == 0:
            return plays.append(playlist)
        else:
            for i in range(len(options)):
                plays_rps(num-1, playlist + [options[i]])
    plays_rps(n)
    return plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
