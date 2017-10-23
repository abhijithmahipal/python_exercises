#Problem 1: Implement a function product to multiply 2 numbers recursively using + and - operators only.

import sys
def product(a,b):
	if(b==0):
		return 0
	elif b<0:
		return -(product(a,-b))
	else:
		return a+product(a,b-1)
		
def main():
	print product(int(sys.argv[1]),int(sys.argv[2]))

main()

