#Problem 2: Python has a built-in function sum to find sum of all elements of a list. Provide an implementation for sum.

def sum1(a):
    value=0
    for i in a:
        value=value+i
    return value

def main():
    print sum1([1,2,3,4])
    print sum1(range(10))
	
if __name__ == '__main__':
    main()
