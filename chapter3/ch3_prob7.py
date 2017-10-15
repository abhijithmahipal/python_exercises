#Problem 7: Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces and special characters are replaced by a hyphen, typically used to create blog post URL from post title. It should also make sure there are no more than one hyphen in any place and there are no hyphens at the biginning and end of the slug.

import sys,re
def makeslug(text):
	print text
	return re.sub('[^A-Za-z0-9]+','-',text)

def main():
	string=(sys.argv[1])
	slug=makeslug(string)
	if slug[0]=='-':
		slug=slug[1:]
	if slug[-1]=='-':
		slug=slug[:-1]
	print slug
	

if __name__=='__main__':
    main()
