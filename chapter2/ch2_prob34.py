#Problem 34: Improve the above program to print the words in the descending order of the number of occurrences.

def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

def read_words(filename):
	return open(filename).read().split()
	
def main(filename):
    frequency = word_frequency(read_words(filename))
    newfrequency=sorted(frequency.items(),key=lambda x: x[1])
    print newfrequency
    for word, count in newfrequency:
        print word, count

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
    

