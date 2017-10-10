#Problem 27: Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet.

def triplet(a):
    a = [(x,y,z) for x in range(1,a) for y in range(x,a) for z in range(a) if x+y==z ] 
    print a

def main():
    triplet(5)

if __name__ == '__main__':
    main()

