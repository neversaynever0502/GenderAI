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


dataAll=[]

data = {"name": "性別工作平等法",
		"content":"雇主對受僱者薪資之給付、退休資遣、離職及解僱，不得因性別或性傾向而有差別待遇。受僱者於執行職務時，任何人以性要求、具有性意味或性別歧視之言詞或行為，雇主違反第七條至第十條、第十一條第一項、第二項者，處新臺幣三十萬元以上一百五十萬元以下罰鍰。",
        "key":txtToArray('word_v1.txt')}
data2 = {"name": "性騷擾防治法",
        "content":"係指性侵害犯罪以外，對他人實施違反其意願而與性或性別有關之行為，且有下列情形之一者：二、以展示或播送文字、圖畫、聲音、影像或其他物品之方式，或以歧視、侮辱之言行，或以他法，而有損害他人人格尊嚴，或造成使人心生畏怖、感受敵意或冒犯之情境，或不當影響其工作、教育、訓練、服務、計畫、活動或正常生活之進行。",
        "key":txtToArray('word_v2.txt')}
data3 = {"name": "刑法第二二一條（強制性交罪）",
        "content":"對於男女以強暴、脅迫、恐嚇、催眠術或其他違反其意願之方法而為性交者，處三年以上十年以下有期徒刑。",
        "key":txtToArray('word_v3.txt')}
data4 = {"name": "刑法第二二四條（強制猥褻罪）",
        "content":"對於男女以強暴、脅迫、恐嚇、催眠術或其他違反其意願之方法，而為猥褻之行為者，處六個月以上五年以下有期徒刑。",
        "key":txtToArray('word_v4.txt')}
data5 = {"name": "刑法第二二五條（乘機性交猥褻罪）",
        "content":"對於男女利用其心神喪失、精神耗弱、身心障礙或其他相類之情形，不能或不知抗拒而為性交者，處三年以上十年以下有期徒刑。",
        "key":txtToArray('word_v5.txt')}
data6 = {"name": "刑法第二二七條（對未成年人為性交猥褻罪）",
        "content":"對於未滿十四歲之男女為性交者，處三年以上十年以下有期徒刑。對於未滿十四歲之男女為猥褻之行為者，處六個月以上五年以下有期徒刑。對於十四歲以上未滿十六歲之男女為性交者，處七年以下有期徒刑。對於十四歲以上未滿十六歲之男女為猥褻之行為者，處三年以下有期徒刑。",
        "key":txtToArray('word_v6.txt')}
data7 = {"name": "刑法第二二八條（利用權勢性交或猥褻罪）",
		"content":"對於因親屬、監護、教養、教育、訓練、救濟、醫療、公務、業務或其他相類關係受自己監督、扶助、照護之人，利用權勢或機會為性交者，處六個月以上五年以下有期徒刑。因前項情形而為猥褻之行為者，處三年以下有期徒刑。",
        "key":txtToArray('word_v7.txt')}
data8 = {"name": "刑法第二二九條（詐術性交罪）",
        "content":"以詐術使男女誤信為自己配偶，而聽從其為性交者，處三年以上十年以下有期徒刑。",
        "key":txtToArray('word_v8.txt')}
data9 = {"name": "刑法第二三一條之一（圖利強制使人性交猥褻罪）",
        "content":"意圖營利，以強暴、脅迫、恐嚇、監控、藥劑、催眠術或其他違反本人意 願之方法使男女與他人為性交或猥褻之行為者，處七年以上有期徒刑，得併科三十萬元以下罰金。",
        "key":txtToArray('word_v9.txt')}
data10 = {"name": "刑法第三三二條第二款（強盜強制性交罪）",
        "content":"犯強盜罪而強制性交者，處死刑或無期徒刑。",
        "key":txtToArray('word_v10.txt')}
data11 = {"name": "刑法第三四八條第二項（擄人勒贖而對被害人強制性交罪）",
        "content":"意圖勒贖而擄人，而對被害人強制性交者，處死刑或無期徒刑。",
        "key":txtToArray('word_v11.txt')}
data12 = {"name": "刑法第二三零條（血親為性交罪）",
        "content":"對直系或三親等內旁系血親為性交者，處五年以下有期徒刑。",
        "key":txtToArray('word_v12.txt')}
data13 = {"name": "刑法第 277 條（普通傷害罪）",
		"content":"傷害人之身體或健康者，處三年以下有期徒刑、拘役或一千元以下罰金。",
        "key":txtToArray('word_v13.txt')}
data14 = {"name": "家庭暴力防治法",
        "content":"指家庭成員間實施身體、精神或經濟上之騷擾、控制、脅迫或其他不法侵害之行為。被害人得向法院聲請通常保護令、暫時保護令；被害人為未成年人、身心障礙者或因故難以委任代理人者，其法定代理人、三親等以內之血親或姻親，得為其向法院聲請之。",
        "key":txtToArray('word_v14.txt')}
data15 = {"name": "刑法第 310 條（誹謗罪）",
        "content":"意圖散布於眾，而指摘或傳述足以毀損他人名譽之事者，為誹謗罪，處一年以下有期徒刑、拘役或五百元以下罰金。散布文字、圖畫犯前項之罪者，處二年以下有期徒刑、拘役或一千元以下罰金。",
        "key":txtToArray('word_v15.txt')}
data16 = {"name": "刑法第 309 條（公然污辱罪）",
        "content":"公然侮辱人者，處拘役或三百元以下罰金。以強暴犯前項之罪者，加重其刑，處一年以下有期徒刑、拘役或五百元以下罰金。",
        "key":txtToArray('word_v16.txt')}
data17 = {"name": "刑法第 235 條（妨害風化罪）",
        "content":"	散布、播送或販賣猥褻之文字、圖畫、聲音、影像或其他物品，或公然陳列，或以他法供人觀覽、聽聞者，處二年以下有期徒刑、拘役或科或併科三萬元以下罰金。",
        "key":txtToArray('word_v17.txt')}
data18 = {"name": "刑法第 315 條（妨害秘密罪）",
        "content":"無故利用工具或設備窺視、竊聽他人非公開之活動、言論、談話或身體隱私部位者，處三年以下有期徒刑，製造、散布、播送或販賣者，處五年以下有期徒刑或五萬元以下罰金。",
        "key":txtToArray('word_v18.txt')}



dataAll.append(data)
dataAll.append(data2)
dataAll.append(data3)
dataAll.append(data4)
dataAll.append(data5)
dataAll.append(data6)
dataAll.append(data7)
dataAll.append(data8)
dataAll.append(data9)
dataAll.append(data10)
dataAll.append(data11)
dataAll.append(data12)
dataAll.append(data13)
dataAll.append(data14)
dataAll.append(data15)
dataAll.append(data16)
dataAll.append(data17)
dataAll.append(data18)

for i in dataAll:
	db.child("laws").push(i)