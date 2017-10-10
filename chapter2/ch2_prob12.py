#Problem 12: Write a function group(list, size) that take a list and splits into smaller lists of given size.

def group(a,b):
    c=[]
    for i in range(0,len(a),b):
        c.append(a[i:i+b])
    return c
        


def main():
    print group([1,2,3,4,5,6,7,8],5)

if __name__ == '__main__':
    main()
