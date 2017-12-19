#! /usr/bin/env python3

import sys

def day2():
	total = 0;
	with open('input.txt') as f:
		for line in f:
			print(line);
			line = line.split()
			if line:
				for i in range(0,len(line)):
					for j in range(0,len(line)):
						if(i != j and (float(line[j])/float(line[i])).is_integer()):
							total += int(line[j])/int(line[i]);
							print(int(line[j])/int(line[i]));
	print(int(total));


def main():
    day2();

if __name__ == '__main__':
    main()