#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-*- MAX Young 2019-09-18  -*-

import requests
from bs4 import BeautifulSoup
import random
import time

proxiesurl = 'http://www.xicidaili.com/nt/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}   

#获取代理ip的list，用于随机选一个
def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    print('get ip list success')
    return ip_list

#随机从获取到的IP中选一个生成代理IP
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    prox = {'http': proxy_ip}
    print('get random ip - success')
    return prox

#刷PV的主程序
def mainpv():
    pvurl = ['https://mikeyoung.zcool.com.cn/',
       'https://www.zcool.com.cn/work/ZMTM0Mzk2MjA=.html',
       'https://www.zcool.com.cn/work/ZODAzODA0MA==.html',
       'https://www.zcool.com.cn/work/ZMTMzNjIwNDQ=.html',
       'https://www.zcool.com.cn/work/ZNzQ2NzA1Mg==.html']
 
    count = 0
    countUrl = len(pvurl) 
    print(proxies)

    #设置一个随机执行的时间
    randomtime = random.randint(1, 100)
    print(randomtime)

    # 访问次数设置限制
    while count < 11:
        try:  # 正常运行
            for i in range(countUrl):
                response = requests.get(pvurl[i], headers=headers,proxies=proxies)
                if response.status_code == 200:
                    count = count + 1
                    print('Success ' + str(count), 'times')
            time.sleep(randomtime)
        except Exception:  # 异常
            print('Failed and Retry')

#运行程序的顺序
if __name__ == '__main__':
    ip_list = get_ip_list(proxiesurl, headers=headers)
    proxies = get_random_ip(ip_list)
    mainpv()

#-*- MAX Young 2019-09-18  -*-

