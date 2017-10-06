#Problem 21: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.

import sys
def wrap(a,s):
	num=int(s)
	f=open(a,'r')
	b=f.readlines()
	for i in b:
		for j in range(0,len(i),num):
			print i[j:j+num]
		
			
def main():
	wrap(sys.argv[1],sys.argv[2])

	
if __name__ == '__main__':
    main()
