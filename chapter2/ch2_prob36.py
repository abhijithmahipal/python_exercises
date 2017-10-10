from ch2_prob10 import unique
def words_frequency(word):
    frequency={}
    for w in word:
        frequency[w]=frequency.get(w,0)+1
    return frequency

def anagrams(words):
    word_dict={}
    anagramlist=[]
    anagram=[]
    for w in words:
        word_dict[w]=words_frequency(w)
    for w in words:
        sublist=[w]
        for x in words:
            if word_dict[w]==word_dict[x]:
                sublist.append(x)
        anagramlist.append(sublist)
    for w in anagramlist:
        anagram.append(unique(sorted(w)))
    print unique(anagram)

def main():
    print anagrams(['eat','ate','car','arc','done','node','soup','tea','done'])


if __name__ == '__main__':
    main()
