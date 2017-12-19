#! /usr/bin/env python3

import sys

INPUT = [c for c in sys.stdin.readline().strip()]

def counter():
	count = 0
	steps_forward = int(len(INPUT)/2)
	for c in INPUT:
		match_num = int(INPUT[(steps_forward)])
		if int(c) == match_num:
			count += int(c)
		steps_forward += 1
		if(steps_forward == len(INPUT)):
			steps_forward = 0

	return count

def main():
    print(counter())

if __name__ == '__main__':
    main()
