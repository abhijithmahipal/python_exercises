#Problem 7: Python has built-in functions min and max to compute minimum and maximum of a given list. Provide an implementation for these functions. What happens when you call your min and max functions with a list of strings?

def min(a, b):
    if a < b:
        return a
    else:
        return b

def max(a, b):
    if a > b:
        return a
    else:
        return b

def main():
    print min(2, 4), max(2, 4), min(4, 2), max(4, 2)
    print min('a', 'b'), max('a', 'b'), min('b', 'a'), max('b', 'a')

if __name__ == '__main__':
    main()
