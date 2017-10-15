#Problem 1: Write a program to list all files in the given directory.

import os
def listDir(path):
    lis= os.listdir(path)
    for i in lis:
        print i

def main():
    listDir('/home/abhijith/Desktop')

if __name__=='__main__':
    main()
