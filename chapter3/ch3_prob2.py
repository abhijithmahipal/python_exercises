#Problem 2: Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.

import os,sys
def listDir(path):
    lis= os.listdir(path)
    return lis

def main():
    files=listDir(sys.argv[1])
    freq={}
    for f in files:
        try:
            l=list(f)   
            a=l.index('.')
            if a==0:
            	continue
            ext=('').join(l[a+1:])
            freq[ext]=freq.get(ext,0)+1
        except ValueError:
            continue
    for key,value in freq.items():
        print key,value

if __name__=='__main__':
    main()

