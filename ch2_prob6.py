#Problem 6: Write a function reverse to reverse a list. Can you do this without using list slicing?

def reversing(a):
    a.reverse()
    return a

def main():
    print reversing([4,5,3,7,5,3])
    print reversing(['q','w','e','r','t','y'])

if __name__ == '__main__':
    main()

