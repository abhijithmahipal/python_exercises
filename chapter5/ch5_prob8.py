#Problem 8: Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.
'''
>>> it = iter(range(5))
>>> x, it1 = peep(it)
>>> print x, list(it1)
0 [0, 1, 2, 3, 4]
'''

def peep(it):
	l=list(it)
	return l[0],iter(l)


def main():
	a,itr=peep(iter([0,1,2,3,4]))
	print a
	print list(itr)

main()




