#Problem 30: Write a python function parse_csv to parse csv (comma separated values) files.

import sys
def parsecsv(a):
    f=open(a,'r')
    b=[]
    c=f.readlines()
    for i in c:
        b.append(i[:-1].split(','))
    print b

def main():
    parsecsv(sys.argv[1])

if __name__ == '__main__':
    main()
