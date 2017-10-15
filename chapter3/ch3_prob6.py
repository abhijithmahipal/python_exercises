#Problem 6: Write a program antihtml.py that takes a URL as argument, downloads the html from web and print it after stripping html tags.
#Downloading and saving in Problem 6. Here a simple HTML page ch3p6.html is opened and stripping its html tags.

import re

def htmlstrip(text):
	return re.sub('<.*?>','',text)

def main():
	f=open('ch3p6.html','r')
	text=f.read()
	strippedtext=htmlstrip(text)
	ff=open('ch3p6.txt','w')
	ff.write(strippedtext)
	ff.close()

if __name__=='__main__':
    main()
    

