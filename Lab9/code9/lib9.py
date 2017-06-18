import functools
import itertools
import collections

def sizes(L):
	return list(map (lambda x:len(x),L))
def pick (L, c):
	return list(filter(lambda x:x[0]==c,L))
def largest(L):
	return (functools.reduce(lambda m,x: x if x>m else m, L))
def product(L1,L2):
	return list(itertools.product(L1,L2))
def isequal(l1,l2):
	#isequal=lambda x,y: collections.Counter(x)==collections.Counter(y)	
	return set(l1)==set(l2) and len(l1)==len(l2)
def split_on_pivot (l, index):
	listsmall=[]
	listgreater=[]
	val=l[index]
	for i in range(0,len(l)):
		if l[i]<val:
			listsmall.append(l[i])
		elif l[i]>val:
			listgreater.append(l[i])
	return [listsmall,listgreater]
def powerset(seq):
	return list(x for x in addon(seq))

def addon(seq):
	if len(seq)<=1:
		yield seq
		yield []
	else:
		for i in powerset(seq[1:]):
			yield [seq[0]]+i
			yield i
def seteq(s1,s2):
	return s1==s2
def build(fname):
	f=open(fname)
	my_dict=dict()
	for line in f:
		key=line.split(':',1)[0]
		value=line.split(':',1)[1]
		my_dict[key]=value
	return my_dict
def getmeaning(dictionary,word):
	if word in dictionary:
		return (dictionary[word])
	else:
		return ("word not found")
def getwords(dictionary,meaning):
	listsym=[';',',','.',':','(',')']
	list2=[]
	for i in dictionary:
		val=dictionary[i]
		list1=val.split(" ")
		for j in range(0,len(list1)):
			if list1[j][-1] in listsym:
				list1[j]=list1[j][:-1]
			elif list1[j][0] in listsym:
				list1[j]=list1[j][1:]
		if meaning in list1:
			list2.append(i)	
	return list2
