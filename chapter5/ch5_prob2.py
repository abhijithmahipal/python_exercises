#Problem 2:Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.

import sys
def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(lines):
    return (line for line in lines if len(line)>40)




def main():
	a=readfiles(sys.argv[1:])
	b=grep(list(a))
	print 'List of Lines having length 40 above: \n',list(b)
	
main()
