#Problem 15: Reimplement the unique function implemented in the earlier examples using sets.

def uniqueset(a):
    b=set()
    for i in a:
        if i not in b:
            b.add(i)
    return b

def main():
    print uniqueset([1,5,5,3,8,5,1,2,2,2,2,3,4,5,5,5,5,5,5,0,6,6,6,6,7])

if __name__ == '__main__':
    main()
