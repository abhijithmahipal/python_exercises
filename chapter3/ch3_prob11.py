#Problem 11: Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.

import urllib,re
def getHtml(url):
	page = urllib.urlopen(url).read()
	print ('').join(re.findall('[0-9]{3}.[0-9]{3}.[0-9]{3}.[0-9]{3}',page))
	



def main():
	getHtml('http://httpbin.org/get')

if __name__=='__main__':
    main()
