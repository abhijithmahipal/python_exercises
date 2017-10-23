#Problem 7: Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.

import sys
def splits(n,filename):
	f=open(filename,'r')
	lines=f.readlines()
	total=len(lines)
	for i in range(0,total+1,n):
		f=open(filename.split('.')[0]+'_'+str(i/n)+'.txt','w')
		try:
			for i in lines[i:i+n]:
				f.write(i)
		except:
			for i in lines[i:]:
				f.write(i)
def main():
	splits(int(sys.argv[1]),sys.argv[2])
main()

