#Problem 4: Write a function to compute the number of python files (.py extension) in a specified directory recursively.


import os,sys

def countpy(dirname):
	count=0
	for dirpath,name,files in os.walk(dirname):
		for f in files:
			if f[-3:]=='.py':
				count+=1
	print count

def main():
	countpy(sys.argv[1])
	
main()


