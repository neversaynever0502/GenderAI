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

wordOrigin1 = ['員工','產假','歧視','同事','主管','職場','女生','男生','辭職']
wordOrigin2 = ['親吻','擁抱','觸摸','臀部','胸部','強制','摸','身體']
wordOrigin3 = ['性交','強姦','強暴','肛門','性器','射精','性器官','輪姦']
wordOrigin4 = ['舌吻','猥褻','脅迫','催眠','脫','口交','摸']
wordOrigin5 = ['精神','心智','缺陷','智障','抗拒','性交','迷昏','昏迷','睡覺','摸','強暴','乘機']
wordOrigin6 = ['未成年','性交','上床','未滿']
wordOrigin7 = ['主管','威脅','上床','強迫','威脅','權勢','口交']
wordOrigin8 = ['欺騙','詐術','性交','強暴','騙','老公','上床']
wordOrigin9 = ['媒婆','媽媽桑','賣淫','妓女','強迫','威脅']
wordOrigin10 = ['搶劫','強盜','偷東西','強姦']
wordOrigin11 = ['綁架','綁票']
wordOrigin12 = ['爸爸','女兒','性交','上床','血親']
wordOrigin13 = ['打','踢','傷害','攻擊']
wordOrigin14 = ['打','踢','保護','保護令','家暴']
wordOrigin15 = ['名譽','抹黑','損毀','散布','毀謗','罵','公開','網路']
wordOrigin16 = ['公開','污辱','抹黑','公開']
wordOrigin17 = ['裸照','色情','散布','網路']
wordOrigin18 = ['偷看','偷','偷拍','隱私']

wordOriginAll = []
wordOriginAll.append(wordOrigin1)
wordOriginAll.append(wordOrigin2)
wordOriginAll.append(wordOrigin3)
wordOriginAll.append(wordOrigin4)
wordOriginAll.append(wordOrigin5)
wordOriginAll.append(wordOrigin6)
wordOriginAll.append(wordOrigin7)
wordOriginAll.append(wordOrigin8)
wordOriginAll.append(wordOrigin9)
wordOriginAll.append(wordOrigin10)
wordOriginAll.append(wordOrigin11)
wordOriginAll.append(wordOrigin12)
wordOriginAll.append(wordOrigin13)
wordOriginAll.append(wordOrigin14)
wordOriginAll.append(wordOrigin15)
wordOriginAll.append(wordOrigin16)
wordOriginAll.append(wordOrigin17)
wordOriginAll.append(wordOrigin18)
# (wordOrigin1,wordOrigin2,wordOrigin3,wordOrigin4,wordOrigin5,wordOrigin6,wordOrigin7,wordOrigin8,wordOrigin9,wordOrigin10,wordOrigin11,wordOrigin12,wordOrigin13,wordOrigin14,wordOrigin15,wordOrigin16,wordOrigin17,wordOrigin18):
for s in range(1,19):
	wordAfter = []
	newS = s-1
	for k in wordOriginAll[newS]:
		try:
			wordAfter.append(model.most_similar(k,topn=10))
		except:
			print("except:"+k)
	# print(wordAfter)
	f = open('word_v'+str(s)+'.txt', 'w')
	for i in wordOriginAll[newS]:
		f.write(i+'\n')
	for i in wordAfter:
		for i2 in i:
			word = i2[0]
			# print (word)
			f.write(word+'\n')
	f.close()
# wordOriginString=""
# count = 0

# for i in wordOrigin:
# 	count = count+1
# 	if count == 1:
# 		wordOriginString = wordOriginString+i
# 	else:
# 		wordOriginString = wordOriginString+" "+i
# print(wordOriginString)
# print(model.most_similar(positive=wordOriginString.split(" "), negative=[u"醫院"],topn=5))

# print(model.most_similar(positive=u"巴黎 柏林".split(" "), negative=[u"法國"],topn=5))

over_time = time.time()

print(over_time-start_time)