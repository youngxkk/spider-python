#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-*- maxc.cc - Max Young 2019-09-18  -*-

from bs4 import BeautifulSoup
import requests
import random

url = 'http://www.xicidaili.com/nt/'
#代理是xicidaili免费的，所以偶尔会报错Connection refused,把url里面的nt换成nn或者wt之类的试试

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
#模仿浏览器操作

#获取ip list
def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

#随机从获取的ip list中选取一个代理ip
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    prox = {'http': proxy_ip}
    return prox

#这个函数只是用来查看ip是否已经代理。
def get_html():
    print(proxies)
    ip138 = requests.get('http://ip111.cn/',proxies=proxies)
    ip138.encoding = 'utf-8' #防止直接print出现乱码
    savehtml = open('ip.txt','wb')
    #查看当前文件夹生成的ip.txt的第58行，是不是与print输出相同？
    savehtml.write(ip138.content)
    savehtml.close
    print('sucess')

if __name__ == '__main__':
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
    get_html()

#-*- Max Young - maxc.cc 2019-09-18  -*-