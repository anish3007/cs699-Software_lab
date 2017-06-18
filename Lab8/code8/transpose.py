import sys

colCount=0
rowCount=0
i=0
inputmat = []

def transpose (inputmat):
	resultmat = [[0 for x in range(rowCount)] for x in range(colCount)]
	for n in range(0, rowCount):
		for x in range(0, colCount):
			resultmat[x][n]=inputmat[n][x]	
	return resultmat



f = open (sys.argv[1])
lines = []
for line in f:
        lines.append(line[:-1]) if line[-1] == "\n" else lines.append(line)

for l in lines: 
	rowCount+=1
	list1=l.split(" ")
	inputmat.append(list1)
	i+=1
	colCount= len(list1)

resultmat=transpose(inputmat)

for n in range(0, len(resultmat)):
	for x in range(0, len(resultmat[n])):
		if (x==rowCount-1):
			print(resultmat[n][x],end="")	
		else:
			print(resultmat[n][x]+" ", end="")
	print()
