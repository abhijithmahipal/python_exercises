#Problem 17: Write a program reverse.py to print lines of a file in reverse order.

import sys
def reverse_str(a):
    f=open(a,'r')
    s=f.read().split('\n')
    s=s[::-1]
    print ('\n').join(s)

def main():
    reverse_str(sys.argv[1])

if __name__ == '__main__':
    main()

