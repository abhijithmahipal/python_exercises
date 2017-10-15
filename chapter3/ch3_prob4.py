#Problem 4: Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree.

import os,sys
def listDir(path):
	lis = os.listdir(path)
	return lis
def printfiles(path1,a):
	files=sorted(listDir(path1),key=lambda x:os.path.isdir(x))
	print files
	print a+'--'+path1.split('/')[-1]
	for f in files:
		if f[0]=='.':
			continue
		if os.path.isdir(path1+'/'+f) :
			a=a+'  |'
			printfiles(path1+'/'+f,a)
		else:
			print a+'--'+f
	return
def main():
	a='|'
	printfiles(sys.argv[1],a)
    
    	
    
    
if __name__=='__main__':
    main()
    
#in line 8 have to sort such that folders come in end
