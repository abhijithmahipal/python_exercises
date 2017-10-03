#Problem 8: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?

def cumulativesum(a):
    value=0
    b = []
    for i in range(len(a)):
        value+=a[i]
        b.append(value)
    return b

def main():
    print cumulativesum([1,2,3,4])

if __name__ == '__main__':
    main()
