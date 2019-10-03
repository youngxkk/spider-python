#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-*- Max Young - maxc.cc 2019-09-18  -*-

import requests
from bs4 import BeautifulSoup

headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36")

page = 0
number = 0
while page < 251:
    url = ("https://movie.douban.com/top250?start=" + str(page) + "&filter=")
    page += 25
    # print(url)
    #下面开始获取url的单独网页
    web_data = requests.get(url) #获取当前url的所有数据
    soup = BeautifulSoup(web_data.text,'lxml') # 用bs4进行网页的标签分析
    info = soup.find_all('div', class_='info') #用soup的find_all功能查找所有class为info的标签内容
    info.encoding = 'utf-8' #防止terminal直接print出现乱码
    savetxt = open('douban.txt','a') #保存到当地的一个txt里便于查看，a是指打开文档，在txt后面添加，w是覆盖。
    for tag in info:
        number += 1 
        # print('5')
        movie_name = tag.find('span', class_='title').get_text() #获得所有标签为title的文本
        movie_rate = tag.find('span', class_='rating_num').get_text() #获得所有标签为rating的内容
        movie_quote = tag.find('span', class_='inq').get_text() #获取标签为inq的内容
        movie_star = tag.find('div', class_='star').get_text() #获取star打分的内容
        moive_star2 = movie_star.find('span')
        # movie_star3 = movie_star2[3].content[0]
        # print(movie_name)
        # 把获取的信息分类后保存到savetxt.txt里面。
        savetxt.write("No" + str(number) + ":    " + str(movie_name) +'     '+ str(movie_rate) +'     '+ str(movie_quote))
        savetxt.write('\n') #这里的\n是换行符
    savetxt.close() #关闭文档
    print(page)



# if __name__ == "__main__":
#     # get_pageurl()
#     movieinfo()