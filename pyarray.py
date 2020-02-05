fileHandler = open("data.dmp","r")
listOfLines = fileHandler.readlines()
f = open("data.dmp","r")
x = []
length=0
for line in listOfLines:
	x.append(line)
	length+=1
for i in range(0,length):
	curLine = f.readline(i)
	if "0x0020" in curLine:
		nobreak = curLine.replace('\n','')
		allInOne = (nobreak) + (f.readline(i+1))
		noTab = allInOne.replace('\t','')
		remNumber = noTab.replace('0x0030:','')
		remNumber2 = remNumber.replace('0x0020:','')
		remDouble = remNumber2.replace('  ',' ')
		print(remDouble) 
		
