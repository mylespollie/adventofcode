#! /usr/bin/env python3

import sys

from itertools import count
from collections import defaultdict

def sum_spiral():
    a, i, j = defaultdict(int), 0, 0
    a[0,0] = 1
    sn = lambda i,j: sum(a[k,l] for k in range(i-1,i+2)
                                for l in range(j-1,j+2))
    for s in count(1, 2):
        for _ in range(s):   i += 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s):   j -= 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s+1): i -= 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s+1): j += 1; a[i,j] = sn(i,j); yield a[i,j]

def part2(n):
    for x in sum_spiral():
        if x>n: return x

def main():
    print(part2(277678));

if __name__ == '__main__':
    main()