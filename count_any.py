ch=raw_input("ENTER A CHARACTER TO BE COUNTER\n")
st=raw_input("\nENTER A LETTER OR PARAGRAPH\n")
count=0
letter=''
for letter in st:
	if letter==ch:
		count=count+1
print "Count of "+ch+" in "+st+" is ",count

