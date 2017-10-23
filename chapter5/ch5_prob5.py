#Problem 5: Write a function to compute the total number of lines of code in all python files in the specified directory recursively.


import os,sys

def countlinespy(dirname):
	count=0
	for dirpath,name,files in os.walk(dirname):
		for f in files:
			if f[-3:]=='.py':
				fp=open(dirpath+'/'+f,'r')
				ln=len(fp.readlines())
				count+=ln
				
	print count

def main():
	countlinespy(sys.argv[1])
	
main()


