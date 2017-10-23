#Problem 9: The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.

import itertools
def my_enum(it):
	it=list(it)
	return itertools.izip(range(len(it)),it)	


def main():
	iterative=my_enum(iter(['a','b','c']))
	print iterative

main()
