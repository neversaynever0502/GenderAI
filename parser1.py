# coding=utf-8

import requests
from urllib3.contrib import pyopenssl
from bs4 import BeautifulSoup
import ssl
import requests.packages.urllib3.util.ssl_

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
head = {"User-gent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}

# res = requests.get("https://news.google.com")
# soup = BeautifulSoup(res.text)
# print (soup.select(".esc-body"))

# count = 1

# for item in soup.select(".esc-body"):
#     print ('======[',count,']=========')
#     news_title = item.select(".esc-lead-article-title")[0].text
#     news_url = item.select(".esc-lead-article-title")[0].find('a')['href']
#     print (news_title)
#     print (news_url)
#     count += 1
# print(ssl.OPENSSL_VERSION)

# with requests.Session() as s:
# 	# data["from"] = "/bbs/Gossiping/index{}.html".format(ind)
# 	s.post("https://www.ptt.cc/ask/over18", headers=head)
# 	res = s.get(link, headers=head)
# 	# soup = BeautifulSoup(res.content,"html.parser")
# 	# data_title = soup.select("div.title")
# s.post("https://www.ptt.cc/ask/over18", data=data, headers=head)
# res = s.get(link, headers=head)

# try:
#     links = ['https://www.ptt.cc/bbs/Gossiping/index' + str(id + 1) + '.html' 
#     for id in range(15156)]
#     twice_link = []
#     data = {"yes": "yes"}
#     head = {"User-gent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
#     for ind, link in enumerate(links, 0):
#        with requests.Session() as s:
#           data["from"] = "/bbs/Gossiping/index{}.html".format(ind)
#           s.post("https://www.ptt.cc/ask/over18", data=data, headers=head)
#           res = s.get(link, headers=head)
#           soup = BeautifulSoup(res.content,"html.parser")
#           data_title = soup.select("div.title")
#           data_date = soup.select("div.date") 
#           data_author =soup.select("div.author")  
#           data_times = soup.select("div.nrec")  
# except Exception as e:
#     print(ssl.OPENSSL_VERSION)
#     print(str(e))


for k in range(1,3220):

	res = requests.get("https://www.ptt.cc/bbs/Boy-Girl/index"+str(k)+".html")
	soup = BeautifulSoup(res.text,'lxml')

	# print (soup)
	# for a in soup.find_all('a', href=True):
	# 	print ("Found the URL:", a['href'])


	for item in soup.select(".r-ent"):
	#     # print ('======[',count,']=========')
		news_title = item.select(".title")[0].text
	# 	# news_url = item.select(".title")[0].find('a')['href']
	# 	# print (news_title)
		print(news_title)
	# 	# print (news_url)
	#     # count += 1