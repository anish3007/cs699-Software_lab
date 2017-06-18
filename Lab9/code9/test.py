import lib9,sys
if len(sys.argv)<2:
	print("Usage: python3 test.py <question_no>")
	exit(0)
if int(sys.argv[1])==1:
	l1=["ahmar","arun","chinmay","jatin","prasanth","samkit","sneha"]
	sample_output = list(lib9.sizes(l1))
	expected_output = [5,4,7,5,8,6,5]
	print("-------------------")
	print("Question No."+sys.argv[1]+"\n-------------------")
	if(sample_output==expected_output):
		print("Testcase 1 passed!")
	else:
		print("Testcase 1 failed")
		print("\tInput: "+str(l1))
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	l2=["ahmar","123",""]
	sample_output = list(lib9.sizes(l2))
	expected_output = [5,3,0]
	if(sample_output==expected_output):
		print("Testcase 2 passed!")
	else:
		print("Testcase 2 failed")
		print("\tInput: "+str(l2))
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))		
	print("-------------------")
elif int(sys.argv[1])==2:
	l1=["ahmar","arun","chinmay","jatin","prasanth","samkit","sneha"]
	sample_output = list(lib9.pick(l1,'a'))
	expected_output = ["ahmar","arun"]
	print("Question No."+sys.argv[1]+"\n-------------------")		
	if(sample_output==expected_output):
		print("Testcase 1 passed!")
	else:
		print("Testcase 1 failed")
		print("\tInput: "+str(l1)+"\t"+'a')
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	sample_output = list(lib9.pick(l1,'s'))
	expected_output = ["samkit","sneha"]
	if(sample_output==expected_output):
		print("Testcase 2 passed!")
	else:
		print("Testcase 2 failed")
		print("\tInput: "+str(l1)+"\t"+'s')
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	print("-------------------")	
elif int(sys.argv[1])==3:
	l1=[2,55,19,32,17]
	sample_output = lib9.largest(l1)
	expected_output = 55
	print("Question No."+sys.argv[1]+"\n-------------------")
	if(sample_output==expected_output):
		print("Testcase 1 passed!")
	else:
		print("Testcase 1 failed")
		print("\tInput: "+str(l1))
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	l2=[-2,-55,-19,-32,-17]
	sample_output = lib9.largest(l2)
	expected_output = -2
	if(sample_output==expected_output):
		print("Testcase 2 passed!")
	else:
		print("Testcase 2 failed")
		print("\tInput: "+str(l2))
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	print("-------------------")
elif int(sys.argv[1])==4:
	l1=[1,2,3]
	l2=['a','b','c']
	sample_output = lib9.product(l1,l2)
	expected_output = [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]
	print("Question No."+sys.argv[1]+"\n-------------------")
	if(sample_output==expected_output):
		print("Testcase 1 passed!")
	else:
		print("Testcase 1 failed")
		print("\tInput: "+str(l1)+"\t"+str(l2))
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	l1 = ["ahmar","arun","jatin",""]
	l2 = [1,2,3,'d']
	sample_output = lib9.product(l1,l2)
	expected_output = [('ahmar', 1), ('ahmar', 2), ('ahmar', 3), ('ahmar', 'd'), ('arun', 1), ('arun', 2), ('arun', 3), ('arun', 'd'), ('jatin', 1), ('jatin', 2), ('jatin', 3), ('jatin', 'd'), ('', 1), ('', 2), ('', 3), ('', 'd')]
	if(sample_output==expected_output):
		print("Testcase 2 passed!")
	else:
		print("Testcase 2 failed")
		print("\tInput: "+str(l1)+"\t"+str(l2))
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	print("-------------------")
elif int(sys.argv[1])==5:
	l1 = [1,2,3]
	l2 = ['1','2','3']
	l3 = [1,2,3]
	sample_output = lib9.isequal(l1,l2)
	expected_output = 0
	print("Question No."+sys.argv[1]+"\n-------------------")
	if(sample_output==expected_output):
		print("Testcase 1 passed!")
	else:
		print("Testcase 1 failed")
		print("\tInput: "+str(l1)+"\t"+str(l2))
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	sample_output = lib9.isequal(l1,l3)
	expected_output = 1
	if(sample_output==expected_output):
		print("Testcase 2 passed!")
	else:
		print("Testcase 2 failed")
		print("\tInput: "+str(l1)+"\t"+str(l3))
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	print("-------------------")
elif int(sys.argv[1])==6:
	l1 = [2,55,19,32,17]
	l2 = [3,1,22,5,7,4]
	sample_output = lib9.split_on_pivot(l1,3)
	expected_output = [[2,19,17],[55]]
	print("Question No."+sys.argv[1]+"\n-------------------")
	if(sample_output==expected_output):
		print("Testcase 1 passed!")
	else:
		print("Testcase 1 failed")
		print("\tInput: "+str(l1)+"\t"+"3")
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	sample_output = lib9.split_on_pivot(l2,4)
	expected_output = [[3,1,5,4],[22]]
	if(sample_output==expected_output):
		print("Testcase 2 passed!")
	else:
		print("Testcase 2 failed")
		print("\tInput: "+str(l2)+"\t"+"4")
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	sample_output = lib9.split_on_pivot(l2,1)
	expected_output = [[],[3,22,5,7,4]]
	if(sample_output==expected_output):
		print("Testcase 3 passed!")
	else:
		print("Testcase 3 failed")
		print("\tInput: "+str(l2)+"\t"+"1")
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	print("-------------------")
elif int(sys.argv[1])==7:
	s1=[1,2,3]
	sample_output = list(lib9.powerset(s1))
	print("Question No."+sys.argv[1]+"\n-------------------")
	for i in sample_output:
		i.sort()
	expected_output = [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]
	flag=0
	for i in sample_output:
		if i not in expected_output:
				flag=1
				print("Testcase 1 failed")
				break
	for i in expected_output:
		if i not in sample_output:
				flag=1
				print("Testcase 1 failed")
				break
	if(flag==0):
		print("Testcase 1 passed!")
	else:
		print("\tInput: "+str(s1))
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	s2=[1,2,3,4]
	sample_output = list(lib9.powerset(s2))
	for i in sample_output:
		i.sort()
	expected_output = [[1,2,3,4], [1,2,3], [1,2,4], [1,3,4],[2,3,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4], [4],[3], [2], [1], []]
	flag=0
	for i in sample_output:
		if i not in expected_output:
				flag=1
				print("Testcase 2 failed")
				break
	for i in expected_output:
		if i not in sample_output:
				flag=1
				print("Testcase 2 failed")
				break
	if(flag==0):
		print("Testcase 2 passed!")
	else:
		print("\tInput: "+str(s2))
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	print("-------------------")
elif int(sys.argv[1])==8:
	s1={1,2,3}
	s2={2,1,3}
	s3={1,2}
	sample_output = lib9.seteq(s1,s2)
	expected_output = 1
	print("Question No."+sys.argv[1]+"\n-------------------")
	if(sample_output==expected_output):
		print("Testcase 1 passed!")
	else:
		print("Testcase 1 failed")
		print("\tInput: "+str(s1)+"\t"+str(s2))
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	sample_output = lib9.seteq(s1,s3)
	expected_output = 0
	if(sample_output==expected_output):
		print("Testcase 2 passed!")
	else:
		print("Testcase 2 failed")
		print("\tInput: "+str(s1)+"\t"+str(s3))
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	print("-------------------")
elif int(sys.argv[1])==9:
	sample_output = lib9.build('dict.txt')
	expected_output = {'mnemonic': 'pertaining to memory; assisting the memory; N: device, such as as formula or rhyme, used as a mnemonic aid\n', 'punctilious': 'minutely attentive (perhaps too much so) to fine points; stressing niceties of conduct or form; N. punctilio, punctiliousness: careful attention payed to every small exact detail\n', 'understate': 'state with less truth than seems warranted by the facts; Ex. He understated the seriousness of the crime; N. understatement; OP. overstate\n', 'protocol': 'diplomatic etiquette; ceremony and etiquette observed by diplomats; first copy of a treaty before its ratification; Ex. Protocol demands that the queen meet him at the airport.\n', 'mores': 'conventions; moral standards; moral customs\n', 'functional': 'made for practical use only (without decoration); functioning; Ex. functional modern furniture; CF. functionalism\n', 'rebuke': 'scold harshly; criticize severely\n', 'imbecility': 'weakness of mind; state of being an imbecile; N. imbecile: stupid person; fool\n', 'braid': 'plait; interweave strands or lengths of; make by weaving strands together; N: braided segment (as of hair)\n', 'contend': 'struggle; compete; assert earnestly; state strongly\n', 'growl': 'low, guttural, menacing sound (as of a dog)\n', 'acquiesce': 'assent; agree passively; comply without protest\n', 'paraphernalia': "equipment; odds and ends used in a particular activity; personal belongings; Ex. photographic paraphernalia; CF. married woman's property exclusive of her dowry\n", 'aviary': 'enclosure for birds; large cage\n', 'bastion': 'stronghold; something seen as a source of protection; Ex. the last bastion of male chauvinism\n', 'adapt': 'make or become suitable for a specific use; alter; modify; adjust; N. adaptation: act of adapting; composition recast into a new form; Ex. The play is an adaption of a short novel.\n', 'maverick': 'rebel; nonconformist (in a group)\n', 'lethargic': 'drowsy; dull; N. lethargy: state of sluggishness and inactivity\n', 'satellite': 'small body revolving around a larger one\n', 'favoritism': 'display of partiality toward a favored person\n', 'timidity': 'lack of self-confidence or courage\n', 'draught': 'current of air (through a room or to a fire); act of pulling roads; act of swallowing liquid or amount of liquid swallowed at a time\n', 'waggish': 'humorous; mischievous; tricky\n', 'conscript': 'draftee; person forced into military service; V.\n', 'betoken': 'signify; indicate; be a sign of\n', 'wake': 'trail of ship or other object through water; path of something that has gone before; Ex. hunger followed in the wake of the war\n', 'reinstate': 'restore to a previous condition or position\n', 'bugaboo': 'bugbear; object of baseless terror\n', 'foliage': 'masses of leaves; CF. defoliate\n', 'bungle': 'mismanage; blunder; botch; blow; spoil by clumsy behavior\n'}
	print("Question No."+sys.argv[1]+"\n-------------------")
	if(sample_output==expected_output):
		print("Dictionary correct!")
	else:
		print("Dictionary incorrect")
		print("\tInput: <dict.txt>")
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	print("-------------------")
elif int(sys.argv[1])==10:
	dictionary = lib9.build('dict.txt')
	w1 = "mnemonic"
	sample_output = str(lib9.getmeaning(dictionary,w1))
	expected_output = "pertaining to memory; assisting the memory; N: device, such as as formula or rhyme, used as a mnemonic aid\n"
	print("Question No."+sys.argv[1]+"\n-------------------")
	if(sample_output==expected_output):
		print("Testcase 1 passed!")
	else:
		print("Testcase 1 failed")
		print("\tInput: <dictionary object built above>"+"\t"+w1)
		print("\tYour output: "+sample_output)
		print("\tExpected output: "+expected_output)
	w2="wake"
	sample_output = str(lib9.getmeaning(dictionary,w2))
	expected_output = "trail of ship or other object through water; path of something that has gone before; Ex. hunger followed in the wake of the war\n"
	if(sample_output==expected_output):
		print("Testcase 2 passed!")
	else:
		print("Testcase 2 failed")
		print("\tInput: <dictionary object built above>"+"\t"+w2)
		print("\tYour output: "+sample_output)
		print("\tExpected output: "+expected_output)
	w3="cs699"
	sample_output = str(lib9.getmeaning(dictionary,w3))
	expected_output = "word not found"
	if(sample_output==expected_output):
		print("Testcase 3 passed!")
	else:
		print("Testcase 3 failed")
		print("\tInput: <dictionary object built above>"+"\t"+w3)
		print("\tYour output: "+sample_output)
		print("\tExpected output: "+expected_output)
	print("-------------------")
elif int(sys.argv[1])==11:
	dictionary = lib9.build('dict.txt')
	w1 = 'the'
	expected_output = ['bastion', 'mnemonic', 'protocol', 'understate', 'wake']
	sample_output = lib9.getwords(dictionary,w1)
	sample_output.sort()
	print("Question No."+sys.argv[1]+"\n-------------------")
	if(sample_output==expected_output):
		print("Testcase 1 passed!")
	else:
		print("Testcase 1 failed")
		print("\tInput: <dictionary object built above>"+"\t"+w1)
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	w2 = 'as'
	expected_output = ['bastion','braid','growl','mnemonic']	
	sample_output = lib9.getwords(dictionary,w2)
	sample_output.sort()
	if(sample_output==expected_output):
		print("Testcase 2 passed!")
	else:
		print("Testcase 2 failed")
		print("\tInput: <dictionary object built above>"+"\t"+w2)
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	w3 = 'cs699'
	expected_output = []	
	sample_output = lib9.getwords(dictionary,w3)
	sample_output.sort()
	if(sample_output==expected_output):
		print("Testcase 3 passed!")
	else:
		print("Testcase 3 failed")
		print("\tInput: <dictionary object built above>"+"\t"+w3)
		print("\tYour output: "+str(sample_output))
		print("\tExpected output: "+str(expected_output))
	print("-------------------")
