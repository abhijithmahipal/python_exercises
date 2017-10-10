#Problem 38: Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.

import sys
def word_frequency(words):
	frequency={}
	for w in words:
		frequency[w]= frequency.get(w,0)+1
	return frequency

def main():
	f=open(sys.argv[1])
	frequency=word_frequency(list(f.read()))
	invert_dict=[(t[1], t[0]) for t in frequency.items()]
	rev_dict=dict(invert_dict)
	print rev_dict
	
if __name__ == '__main__':
	main()
