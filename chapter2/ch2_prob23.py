#Problem 23: Write a program center_align.py to center align all lines in the given file.

import sys
def wrapword(a):
	f=open(a,'r')
	b=f.read().split('\n')
	length=[len(i) for i in b]
	maxlength=max(length)
	for i in b:
		while len(i)<maxlength+2:
			i=' '+i+' '
		print i
		

		
		
		

			
def main():
	wrapword(sys.argv[1])

	
if __name__ == '__main__':
    main()
