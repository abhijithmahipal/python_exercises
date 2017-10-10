#Problem 13: Write a function lensort to sort a list of strings based on length.

def lensort(a):
    a.sort(key=len)
    return a

def main():
    print lensort(['a','bb','c','fffffff','dfdfs','dsssssssssss'])

if __name__=='__main__':
    main()
