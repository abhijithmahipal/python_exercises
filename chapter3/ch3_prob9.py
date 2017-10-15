#Problem 9: Write a regular expression to validate a phone number.
import sys,re
	
def validate(num):
	if re.match('(^[1-9])([0-9]{9}$)',num):
		print 'Valid'
	else:
		print 'Invalid'
	
 	

def main():
	num=sys.argv[1]
	validate(num)

if __name__=='__main__':
    main()
