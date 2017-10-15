#Problem 10: Write a program myip.py to print the external IP address of the machine. Use the response from http://httpbin.org/get and read the IP address from there. The program should print only the IP address and nothing else.

import urllib,re
def getHtml(url):
	page = urllib.urlopen(url).read()
	print ('').join(re.findall('[0-9]{3}.[0-9]{3}.[0-9]{3}.[0-9]{3}',page))
	



def main():
	getHtml('http://httpbin.org/get')

if __name__=='__main__':
    main()
