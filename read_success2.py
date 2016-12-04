# -*- coding:utf8
from gensim import models
import time
start_time = time.time()
print ('Step1:Read your dictionary results..')

model = models.word2vec.Word2Vec.load('/Volumes/SPACE/word2vecAndGieba/test1116_summary/vector_for_word_training/3_wikiTrain/dictionary_dim_100_fast',mmap='r')

# def txtToArray(filename):
# 	f = open(filename, 'r+')
# 	array=[]
# 	for line in f:
# 		array.append(line.replace('\n',''))
# 	return array

# print(txtToArray('word_v1.txt'))

wordOrigin = ['家暴','打人','巴掌','拳','踢','打']
wordAfter = []
for k in wordOrigin:
	wordAfter.append(model.most_similar(k,topn=10))

# print(wordAfter)
f = open('word_v2.txt', 'w')
for i in wordOrigin:
	f.write(i+'\n')
for i in wordAfter:
	for i2 in i:
		word = i2[0]
		# print (word)
		f.write(word+'\n')
f.close()
wordOriginString=""
count = 0

for i in wordOrigin:
	count = count+1
	if count == 1:
		wordOriginString = wordOriginString+i
	else:
		wordOriginString = wordOriginString+" "+i
# print(wordOriginString)
print(model.most_similar(positive=wordOriginString.split(" "), negative=[u"醫院"],topn=5))

# print(model.most_similar(positive=u"巴黎 柏林".split(" "), negative=[u"法國"],topn=5))

over_time = time.time()

print(over_time-start_time)