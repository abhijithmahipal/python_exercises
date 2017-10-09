#Problem 35: Write a program to count frequency of characters in a given file. 

def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

def read_words(filename):
	f= open(filename)
	chars=list(f.read())
	return chars
def main(filename):
	frequency=word_frequency(read_words(filename))
	for keys,values in sorted(frequency.items(),key=lambda s: s[0].lower()):
		print keys,values
	
if __name__ == "__main__":
    import sys
    main(sys.argv[1])
    
#Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?

