#Problem 19: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.

import sys
def head(a):
	f=open(a,'r')
	s=f.read().split('\n')
	print ('\n').join(s[:10])
    
def tail(a):
	f=open(a,'r')
	s=f.read().split('\n')
	print ('\n').join(s[-11:])

def main():
	print '\nHead\n'
	head(sys.argv[1])
	print '\nTail\n'
	tail(sys.argv[1])
	
if __name__ == '__main__':
    main()

