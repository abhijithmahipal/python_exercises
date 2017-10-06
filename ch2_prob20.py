#Problem 20: Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.

import sys
def grep(a,s):
	f=open(a,'r')
	b=f.readlines()
	for i in b:
		if s in i:
			print i
			
def main():
	grep(sys.argv[1],sys.argv[2])

	
if __name__ == '__main__':
    main()
