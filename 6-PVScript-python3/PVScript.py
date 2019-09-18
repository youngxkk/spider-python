#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import time
 
url = ['https://mikeyoung.zcool.com.cn/',
       'https://www.zcool.com.cn/work/ZMTM0Mzk2MjA=.html',
       'https://www.zcool.com.cn/work/ZODAzODA0MA==.html',
       'https://www.zcool.com.cn/work/ZMTMzNjIwNDQ=.html',
       'https://www.zcool.com.cn/work/ZNzQ2NzA1Mg==.html']
 
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}   
 
count = 0
countUrl = len(url)
 
# 访问次数设置
while count < 18:
    try:  # 正常运行
        for i in range(countUrl):
            response = requests.get(url[i], headers=headers)
            if response.status_code == 200:
                count = count + 1
                print('Success ' + str(count), 'times')
        time.sleep(62)
 
    except Exception:  # 异常
        print('Failed and Retry')
