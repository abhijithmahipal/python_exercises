#Problem 11: Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.

import zipfile,sys
def archieve(files,filename):
	z=zipfile.ZipFile(filename,'w')
	for a in files:
		z.write(a, compress_type=zipfile.ZIP_DEFLATED)
	
def main():
	files=sys.argv[2:]
	filename=sys.argv[1]
	archieve(files,filename)

if __name__=='__main__':
    main()
