#Problem 11: Write a function dups to find all duplicates in the list.


def dups(a):
    b=[]
    while len(a) > 0:
        c=a.pop(0)
        if c not in b and c in a:
            b.append(c)
    return b




def main():
    print dups([1,2,4,6,3,4,2,66])

if __name__ == '__main__':
    main()
