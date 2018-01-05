#! /usr/bin/env python3


import sys
from copy import deepcopy
import numpy
import itertools

banks = [int(x) for x in sys.stdin.readline().split()]
def day6():
    count = 0
    count2 = 0
    seen = {}
    seen2 = {}
    while tuple(banks) not in seen:
        seen[tuple(banks)] = count
        i, m = max(enumerate(banks), key=lambda k: (k[1], -k[0]))
        banks[i] = 0
        for j in itertools.islice(itertools.cycle(range(len(banks))), i + 1, i + m + 1):
            banks[j] += 1
        count += 1
    banks2 = banks
    while tuple(banks2) not in seen2:
        seen2[tuple(banks2)] = count
        i, m = max(enumerate(banks2), key=lambda k: (k[1], -k[0]))
        banks2[i] = 0
        for j in itertools.islice(itertools.cycle(range(len(banks2))), i + 1, i + m + 1):
            banks2[j] += 1
        count2 += 1
    print(banks2);
    return count2;

def main():
    print(day6())


if __name__ == '__main__':
    main()

