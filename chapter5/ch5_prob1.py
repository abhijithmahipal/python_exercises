#Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. ::

class rev_iter:
    def __init__(self, l):
    	self.l=l
    	self.i=0
        self.length = len(l)

    def __iter__(self):
        return self

    def next(self):
    	
        if self.i < self.length:
			res=self.l[self.i]
			self.i=self.i+1
			return res
        else:
            raise StopIteration()
           
a=rev_iter([1,2,3,4,5])
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()




