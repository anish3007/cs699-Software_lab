import sys

colCount1=0
rowCount1=0
colCount2=0
rowCount2=0
mat1 = []
mat2 = []

def matmult (mat1,mat2): 
	if(colCount1 != rowCount2):
		return "ERROR"
	
	result = [[0 for x in range(colCount2)] for x in range(rowCount1)]
	for i in range(len(mat1)):
	   for j in range(len(mat2[0])):
	       for k in range(len(mat2)):		   
	           result[i][j] += mat1[i][k] * mat2[k][j]
	return result


#Read first file into mat1
f = open (sys.argv[1])
lines = []
for line in f:
        lines.append(line[:-1]) if line[-1] == "\n" else lines.append(line)

for l in lines: 
	rowCount1+=1
	list1=l.split(" ")
	mat1.append(list1)
	colCount1= len(list1)

for n in range(0, len(mat1)):
	for x in range(0, len(mat1[n])):
		mat1[n][x]=int(mat1[n][x])

#Read second file into mat2
f = open (sys.argv[2])
lines = []
for line in f:
        lines.append(line[:-1]) if line[-1] == "\n" else lines.append(line)

for l in lines: 
	rowCount2+=1
	list2=l.split(" ")
	mat2.append(list2)
	colCount2= len(list2)

for n in range(0, len(mat2)):
	for x in range(0, len(mat2[n])):
		mat2[n][x]=int(mat2[n][x])

result=matmult(mat1,mat2)

out=open(sys.argv[3],"w")
orig_stdout = sys.stdout
sys.stdout = out

if(result!="ERROR"):
	for n in range(0, len(result)):
		for x in range(0, len(result[n])):
			if (x==len(result[n])-1):
				print(str(result[n][x]))	
			else:
				print(str(result[n][x])+" ", end="")				
		
else:
	print("ERROR")

sys.stdout = orig_stdout
out.close()
