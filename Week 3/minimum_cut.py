import random

def checkSelfLoops(checkDict):
	for key in checkDict:
		checkDict[key] = [y for y in checkDict[key] if y != key]
	return checkDict

def replaceItem(lst, itemIn, itemOut):
	for i in range(len(lst)):
		if lst[i] == itemOut:
			lst[i] = itemIn
	return lst

def permutDict(checkDict, vertIn, vertOut):
	checkDict[vertIn].extend(checkDict[vertOut])
	for item in checkDict[vertOut]:
		if item != vertOut:
			checkDict[item] = replaceItem(checkDict[item], vertIn, vertOut)
	checkSelfLoops(checkDict)
	checkDict.pop(vertOut)
	return checkDict


def min_cut(inp):
	while (len(inp.keys()) > 2):
		randomEdge_1 = random.choice(list(inp.keys()))
		randomEdge_2 = random.choice(inp[randomEdge_1])
		inp = permutDict(inp, randomEdge_1, randomEdge_2)
	return inp


f = open('kargerMinCut.txt', 'r')
lst = f.readlines()
for i in range(len(lst)):
	lst[i] = lst[i].split()
	for j in range(len(lst[i])):
		lst[i][j] = int(lst[i][j])

myDict = {}

for i in range(len(lst)):
	myDict[i + 1] = lst[i]

dict1 = myDict.copy()
dict1 = min_cut(dict1)
length = len(dict1[list(dict1.keys())[1]])
print(length)

f.close()	