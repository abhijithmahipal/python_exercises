#Problem 29: Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:

def array2d(i, j):
    a=[[None for y in range(j)] for x in range(i)]
    print a

def main():
    array2d(4,7)

if __name__ == '__main__':
    main()
