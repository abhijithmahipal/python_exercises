#Problem 5: Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?

import ch2_prob4 as mod

def factorial1(a):
    return mod.product1(range(1,a+1))

def main():    
    print factorial1(7)

if __name__ == '__main__':
    main()
