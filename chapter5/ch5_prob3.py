#Problem 3: Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.


import os,sys

def findfiles(dirname):
	for dirpath,dirs,files in os.walk(dirname):
		if dirpath[-1]=='/':
			dirpath=dirpath[:-1]
		for f in files:
			yield dirpath+'/'+f


for i in findfiles(sys.argv[1]):
	print(i)
