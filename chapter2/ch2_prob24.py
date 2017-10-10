#Provide an implementation for zip function using list comprehensions.

def zip_funtion(a,b):
    minlen=min(len(a),len(b))
    c=[(a[i],b[i]) for i in range(minlen)]
    print c

def main():
    zip_funtion([1,2,3,4,5],[6,7,4,5,8,9,0])

if __name__ == '__main__':
    main()
