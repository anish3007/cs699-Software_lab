import sys

def fibindex (number):
	a,b=0,1
	i=-1
	while a<number:
		a,b=b,a+b
		i=i+1
	if a==number:
		result=i+1
	else:
		result=-1
	return result


num=int(sys.argv[1])
result=fibindex(num)
if(result==-1):
	print("NOT FOUND")
else:
	print (result)
