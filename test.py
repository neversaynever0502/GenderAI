def txtToArray(filename):
	f = open(filename, 'r+')
	array=[]
	for line in f:
		array.append(line.replace('\n',''))
	return array

sex = txtToArray('word_v1.txt')
violent = txtToArray('word_v2.txt')

question = ['今天','我','被','我','老公','打了一頓','拳','打','腳','踢','該','怎麼辦']


import math
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

print('跟性侵的相似度：')
print(similar(sex,question))
print('跟家暴的相似度：')
print(similar(violent,question))
if similar(sex,question)>similar(violent,question):
	print('此題是性侵相關法律')
else:
	print('此題是家暴相關法律')