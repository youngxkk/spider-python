#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tool
from bs4 import BeautifulSoup
import time
import os

# 定义要创建存图片的目录，当前文件夹下
folder = 'pic/'

#你想要爬取的花瓣画板的 url **
base_url = 'http://huaban.com/boards/46470426/'

def genUrl(id):
    print id
    if id == 11111111111111:
        return False
    return base_url+'/?&max='+str(id)+'&limit=20&wfl=1'

def getUrl(pageUrl):
    html = Tool.crawl(pageUrl)
    if html:
        soup = BeautifulSoup(html, 'lxml')
        min = 11111111111111
        for div in soup.select('.pin.wfc'):
            a = int(div.attrs['data-id'])
            if a < min:
                min = a
        i = 1
        for imgDiv in soup.select('.img.layer-view img'):
            imgUrl = imgDiv.attrs['src'].replace('//','http://').replace('_fw236','')
            print imgUrl
            Tool.down(imgUrl,folder+str(int(time.time()*1000))+str(i)+'.jpeg')
            i = i + 1
        
        return genUrl(min)

def mkdir(path):
    path=path.strip() 
    path=path.rstrip("\\") 
    isExists=os.path.exists(path)
 
    if not isExists:   
        print path+' 创建成功' 
        os.makedirs(path) 
        return True
    else:
        print path+' 目录已存在' 
        return False

if __name__ == '__main__':
    mkdir(folder)
    url = genUrl(11111111111112)
    while url:
        print url
        url = getUrl(url)

        
# -*- zhaoyahong & yangxingkong2019-3-20 -*-