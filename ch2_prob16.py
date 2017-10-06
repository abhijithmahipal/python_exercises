#Problem 16: Write a function extsort to sort a list of files based on extension.


def extsort(a):
	def splits(b):
		c=b.split('.')
		return c[1]
	a.sort(key=splits)
	return a

def main():
    print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])

if __name__ == '__main__':
    main()








