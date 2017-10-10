#Problem 25: Python provides a built-in function map that applies a function to each element of a list. Provide an implementation for map using list comprehensions.

def map_fun(a,b):
    print [a(i) for i in b]

def square(x):
    return x*x

def main():
    map_fun(square,range(10))

if __name__ == '__main__':
    main()
