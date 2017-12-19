#! /usr/bin/env python3


import sys

INPUT = [int(c) for c in sys.stdin.readlines()]

def day5():
    index = 0;
    steps = 0;
    while (index < len(INPUT)):
        temp_index = index;
        index = index + INPUT[index];
        if(INPUT[temp_index] >= 3):
            INPUT[temp_index] = INPUT[temp_index]-1;
        else:
            INPUT[temp_index] = INPUT[temp_index]+1;
        steps = steps+1;
    return steps;

def main():
    print(day5())


if __name__ == '__main__':
    main()

