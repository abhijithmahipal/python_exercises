#Problem 28: Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.

def enumerate_fn(a):
    print [i for i in zip(range(len(a)),a)]

def main():
    enumerate_fn(list('HelloWorld'))

if __name__ == '__main__' :
    main()
