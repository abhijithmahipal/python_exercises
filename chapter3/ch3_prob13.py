#Problem 13: Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as the second argument.

import sys,tablib
def csv2xls(csvname,xlsname):
	data = tablib.Dataset()
	with open(csvname,'r') as f:
		data.csv =f.read()
	with open(xlsname,'wb') as f:
		f.write(data.xls)
	
	
def main():
	csvname=sys.argv[1]
	xlsname=sys.argv[2]
	csv2xls(csvname,xlsname)
	
if __name__=='__main__':
    main()
