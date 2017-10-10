#Problem 4: Implement a function product, to compute product of a list of numbers.

def product1(a):
    value=1
    for i in a:
        value*=i
    return value

def main():
    print product1([1,2,3,4])
    print product1(range(10)[1:21])

if __name__ == '__main__':
    main()
