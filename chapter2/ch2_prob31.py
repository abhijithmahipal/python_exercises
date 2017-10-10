#Problem 31: Generalize the above implementation of csv parser to support any delimiter and comments.

import sys
def parsecsv(a,d):
    f=open(a,'r')
    b=[]
    c=f.readlines()
    for i in c:
        b.append(i[:-1].split(d))
    print b

def main():
    parsecsv(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
    main()

