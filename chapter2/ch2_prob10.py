#Problem 10: Write a function unique to find all the unique elements of a list.

def unique(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b

def main():
    print unique([1,1,2,2,2,2,3,4,5,5,5,5,5,5,0,6,6,6,6,7])

if __name__ == '__main__':
    main()
