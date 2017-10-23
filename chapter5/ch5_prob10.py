#Problem 10: Implement a function izip that works like itertools.izip.


def izip(l1,l2):
	join=[(l1[i],l2[i]) for i in range(len(l1))]
	return iter(join)


def main():
	it=izip([1,2,3,4],['a','b','c','d'])
	print it
main()

