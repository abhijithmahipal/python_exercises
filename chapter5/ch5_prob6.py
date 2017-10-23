#Problem  6: Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.


import os,sys

def countspecialpy(dirname):
	count=0
	for dirpath,name,files in os.walk(dirname):
		for f in files:
			if f[-3:]=='.py':
				fp=open(dirpath+'/'+f,'r')
				lin=fp.readlines()
				for l in lin:
					if l[0]=='#' or len(l)==1:
						continue
					count+=1
				
	print count

def main():
	countspecialpy(sys.argv[1])
	
main()


