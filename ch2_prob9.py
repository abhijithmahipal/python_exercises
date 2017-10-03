#Problem 9: Write a function cumulative_product to compute cumulative product of a list of numbers.

def cumulativesum(a):
    value=1
    b = []
    for i in range(len(a)):
        value*=a[i]
        b.append(value)
    return b

def main():
    print cumulativesum([9,5,6,2,3,4])

if __name__ == '__main__':
    main()

