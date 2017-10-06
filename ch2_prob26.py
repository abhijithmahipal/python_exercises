#Problem 26: Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions.

def odd(x):
    return x %2 != 0

def filter_function(a,b):
    print [i for i in b if a(i)]

def main():
    filter_function(odd,range(17))

if __name__ == '__main__' : 
    main()

