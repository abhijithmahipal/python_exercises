#Problem 3: Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.

import os,sys
def listDir(path):
    lis = os.listdir(path)
    return lis

def main():
    files=listDir(sys.argv[1])
    for f in files:
    	stat=os.stat(sys.argv[1]+'/'+f)
    	line=f+'\t'+str(stat[6])+'\t'+str(stat[8])
    	print line
if __name__=='__main__':
    main()

