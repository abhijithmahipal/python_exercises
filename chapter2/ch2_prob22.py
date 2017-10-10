#Problem 22: The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?

import sys
def wrapword(a,s):
	num=int(s)
	f=open(a,'r')
	b=f.read().split('\n')
	c=(' ').join(b)
	d=c.split(' ')
	#Now d is a list of words without white spaces
	e=''
	i=0
	while i < len(d):
		e=e+d[i]
		if len(e)<num:
			e=e+' '
			i+=1
		else:
			e=e+'\n'
			print e
			e=''
			i+=1

			
def main():
	wrapword(sys.argv[1],sys.argv[2])

	
if __name__ == '__main__':
    main()
