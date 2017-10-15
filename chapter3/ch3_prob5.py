#Problem 5: Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.

import urllib,sys

def getHtml(url):
	namecheck=(url+' ').split('/')[-1]
	if namecheck==' ':
		name='index.html'
	else:
		name=namecheck
	f=open(name,'w')
	page = urllib.urlopen(url)
	pagetext=page.read() 
	f.write(pagetext)
	f.close()
 	

def main():
	url=sys.argv[1]
	getHtml(url)
	
    
    
if __name__=='__main__':
    main()
    

