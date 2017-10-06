#Problem 18: Write a program to print each line of a file in reverse order.

import sys

def reverse_each(a):
	f = open(a,'r')
	b=f.read().split('\n')
	c=[i[::-1] for i in b]
	print ('\n').join(c)

def main():
    reverse_each(sys.argv[1])

if __name__ == '__main__':
    main()

