# -*- coding:utf8
import pyrebase
import xlrd
from openpyxl import load_workbook
from openpyxl.writer.excel import ExcelWriter
from openpyxl.workbook import Workbook


config = {
  "apiKey": "AIzaSyCj1XmaKWQcZ_RGrYpNPlDb6JXq_mQk9Do",
  "authDomain": "codeforgenderhackthon.firebaseapp.com",
  "databaseURL": "https://codeforgenderhackthon.firebaseio.com",
  "storageBucket": "codeforgenderhackthon.appspot.com"
}

# wb =load_workbook(filename = '性侵害事件通報被害及加害人概況.xls')

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def txtToArray(filename):
	f = open(filename, 'r+')
	array=[]
	for line in f:
		array.append(line.replace('\n',''))
	return array

print(txtToArray('word_v1.txt'))


# dataAll=[]

# data = {"name": "性別工作平等法",
# 		"content":"雇主對受僱者薪資之給付、退休資遣、離職及解僱，不得因性別或性傾向而有差別待遇。受僱者於執行職務時，任何人以性要求、具有性意味或性別歧視之言詞或行為，雇主違反第七條至第十條、第十一條第一項、第二項者，處新臺幣三十萬元以上一百五十萬元以下罰鍰。",
#         "key":txtToArray('word_v1.txt')}



# dataAll.append(data)

db.child("discriminations").push(txtToArray('word_nogood.txt'))