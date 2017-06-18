import sys
import math


def binsearch (inputlist,number): 
	result = -1
	low=0
	high=len(inputlist)-1	

	while(low <= high):
		mid=int(math.floor((low+high)/2))
		if(number == int(inputlist[mid])):
			return mid
		elif(number < int(inputlist[mid])):
			high=mid-1
		else:
			low=mid+1
	return result


#Read file
f = open (sys.argv[1])
lines = []
for line in f:
        lines.append(line[:-1]) if line[-1] == "\n" else lines.append(line)
list1 = []
for l in lines: 
	list1=l.split(" ")


for i in range(0,len(list1)):
	list1[i]=int(list1[i])

num=int(sys.argv[2])
list1=sorted(list1)
result=binsearch(list1,num)

if(result!=-1):
	print(result)		
else:
	print("NOT FOUND")
