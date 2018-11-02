import Tool
from bs4 import BeautifulSoup
import time

folder = 'pics/'
base_url = 'http://huaban.com/boards/47779150/'

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

if __name__ == '__main__':
    url = genUrl(11111111111112)
    while url:
        print url
        url = getUrl(url)
