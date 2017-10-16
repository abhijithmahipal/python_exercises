#Problem 12: Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.

import inspect,sys,importlib
def mydoc(mod):
	impmod=importlib.import_module(mod)
	print 'Module '+mod
	print '\nDescription: \n\n'+impmod.__doc__
	modobjects=dir(impmod)
	for i in modobjects:
		attr=getattr(impmod,i)
		if inspect.isfunction(attr):
			print i+'()'
	
	
def main():
	mydoc(sys.argv[1])

if __name__=='__main__':
    main()
