#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os

def get_link(id):
	urlfront = "https://www.i4.cn/wper_1_0_0_"
	urlback = ".html"
	mainurl = urlfront + id + urlback
	print(mainurl)
	return mainurl

# 获取图片的链接
def get_html(url):

	#获取网页请求
	res = requests.get(url) 
	# res.encoding='utf-8'
	# 模拟浏览器操作
	i_headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}

	#将网页转化为soup对象标准xml输出
	soup = BeautifulSoup(res.text, 'html.parser') 
	
	#找到所有img标签，并且class=wper_img的项
	src = soup.find_all('img', class_="wper_img")
	print(len(src))
	return src

def download(links):
	n = 1
	# 遍历文档,获取链接的组合

	for link in links: 
		#获取标签为data-big的文本
		img_url = link.get('data-big')

		#获取图片的文件名
		pic_name = img_url[-22:]
		print('正在下载第 %d 张图片啦啦啦' % n)
		
		#获取image二进制流数据
		picres = requests.get(img_url).content
		
		file = open(pic_name,'wb')	#创建图片
		file.write(picres)	#写入
		
		n = n + 1

	file.close() #关闭

def start():
	for x in range(1,20):
		num = str(x)
		baseurlll = get_link(num)
		x = x + 1
		print('正在下载第 %s 页' % x)
		baseurl = get_html(baseurlll)
		download(baseurl)

if __name__ == '__main__':
	start()
	# num = str(input('说吧想爬取哪一页:'))
	# print(num)
	# baseurlll = get_link(num)
	# baseurl = get_html(baseurlll)
	# download(baseurl)