#Problem 14: Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.

def unique(a,key):
    d=[key(i) for i in a]
    b=[]
    for i in d:
        if i not in b:
            b.append(i)
    return b

def main():
    print unique(["python",'C', "java", "Python", "Java"], key=lambda s: s.lower())

                                                
if __name__ == '__main__':
    main()
