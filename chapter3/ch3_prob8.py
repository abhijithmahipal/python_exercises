#Problem 8: Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.

import sys,re,urllib
	
def getlinks(url):
	page = urllib.urlopen(url)
	pagetext=page.read()
	pagetexts = re.findall('"http.*"',pagetext)
	for i in pagetexts:
		print i
 	

def main():
	url=sys.argv[1]
	getlinks(url)

if __name__=='__main__':
    main()
