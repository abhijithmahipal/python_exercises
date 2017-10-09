#Problem 37: Write a function valuesort to sort values of a dictionary based on the key.

import sys
def word_frequency(words):
	frequency={}
	for w in words:
		frequency[w]= frequency.get(w,0)+1
	return frequency

def main():
	f=open(sys.argv[1])
	frequency=word_frequency(f.read().split())
	for key,value in sorted(frequency.items()):
		print value

if __name__ == '__main__':
	main()
