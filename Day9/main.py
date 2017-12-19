#! /usr/bin/env python3


import sys


INPUT = [c for c in sys.stdin.readline().strip()]

def solve():
    score = level = 0
    ignoreNext = inGarbage = False
    garbocount = 0
    for c in INPUT:
        if ignoreNext:
            ignoreNext = False
            continue

        if inGarbage and c != '>':
            if c == '!': ignoreNext = True;
            else: garbocount += 1
            continue

        if c == '!': ignoreNext = True
        elif c == '<': inGarbage = True
        elif c == '>': inGarbage = False
        elif c == '{': level += 1
        elif c == '}': score += level; level -= 1

    return([garbocount])

def main():
    print(solve())


if __name__ == '__main__':
    main()

