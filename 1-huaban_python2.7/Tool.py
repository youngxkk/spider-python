# coding=utf-8
import urllib2
import logging, time
import ssl
import socket


def getLastFromUrl(url):
    if url:
        return url[url.rfind('/') + 1:]
    return ''

def crawl(pageurl, times=0):
    if times > 5:
        log_warn("page failed:" + pageurl)
        return False
    try:
        page = urllib2.urlopen(pageurl, None, 10)
        return page.read()
    except urllib2.HTTPError, e:
        if e.code == 404:
            return False
        else:
            return crawl(pageurl, times + 1)
    except urllib2.URLError, e:
        return crawl(pageurl, times + 1)
    except ssl.SSLError, e:
        return crawl(pageurl, times + 1)

def down(url, file):
    try:
        page = urllib2.urlopen(url, None, 100)
        img = page.read()
        with open(file, 'wb') as f:
            f.write(img)
    except urllib2.HTTPError, e:
        if e.code == 404:
            return False
        else:
            return False
    except urllib2.URLError, e:
        return False
    except socket.timeout, e:
        return False

def log_info(d):
    info = now() + d
    logging.info(info)

def log_warn(d):
    warn = now() + d
    logging.warn(warn)
    print warn

def now():
    return time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(time.time()))

if __name__ == '__main__':
    pass


# -*- yahong & yangxingkong-2018-12-20 -*-