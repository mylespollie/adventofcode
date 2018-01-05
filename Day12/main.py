#! /usr/bin/env python3

import sys

INPUT = [c.strip() for c in sys.stdin.readlines()]

def day12():
	arr = []
	arr.append(0);
	for i in range(0,len(INPUT)):
		pipe, talks_to = INPUT[i].split(' <-> ');
		pipe=int(pipe);
		arr2 = [int(c) for c in talks_to.split(',')]
		print(pipe);
		print(arr);
		print(pipe in arr);
		if(pipe == 0):
			print(pipe);
			print(arr2);
			arr.append(arr2);
		elif(pipe in arr):
			print(pipe);
			print(arr2);
			arr.append(arr2);




def main():
    print(day12())

if __name__ == '__main__':
    main()
