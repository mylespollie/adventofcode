#! /usr/bin/env python3

import sys

def day3():
	direction = 'right';
	values[0][0] = 1;
	i = 0;
	j = 0;
	while value <= 277678:
		new_val = 0;
		if(values[i+1][j]):
			new_val += values[i+1][j];
		if(values[i-1][j]):
			new_val += values[i-1][j];
		if(values[i][j+1]):
			new_val += values[i][j+1];
		if(values[i][j-1]):
			new_val += values[i][j-1];
		if(direction == 'right'):
			values[i+1][j] = new_val
		else if(direction == 'up'):
			values[i][j+1] = new_val
		else if(direction == 'left'):
			values[i-1][j] = new_val
		else if(direction == 'down'):
			values[i+1][j] = new_val

def main():
    day3();

if __name__ == '__main__':
    main()