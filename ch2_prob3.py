#Problem 3: What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.

def sum2(a):
    value=a[0]
    for i in a[1:]:
        value=value+i
    return value
    
def main():
    print sum2(['a','b','c'])
    print sum2([1,2,3,4])
	
if __name__ == '__main__':
    main()
