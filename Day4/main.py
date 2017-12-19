#! /usr/bin/env python3

import sys

def anagrams(str1, str2):
	print(str1, ' ', str2)
	if(sorted(str1) == sorted(str2)):
		print("TRUE");
		return True;
	else:
		print("FALSE");
		return False;


def day4():
	total = 0;
	with open('input.txt') as f:
		for line in f:
			line = line.split()
			if line:
				valid = True;
				for i in range(0,len(line)):
					for j in range(0,len(line)):
						if(i!=j and line[i] == line[j]):
							valid = False;
						if(i!=j and anagrams(line[i], line[j])):
							valid = False;
			if(valid):
				total = total+1;
	print(int(total));


def main():
    day4();

if __name__ == '__main__':
    main()