import requests
from bs4 import BeautifulSoup
import time

rootUrl = 'http://pyqt.sourceforge.net/Docs/PyQt4/'

proxy = {
    'http': 'http://jp.gfw.li:25'
}

classList = []
MD = open('README.md', 'w+')

r = requests.get(rootUrl+'classes.html', proxies=proxy)
# r = requests.get(rootUrl+'classes.html')
soup = BeautifulSoup(r.text)
for a in soup.findAll('table')[1].findAll('a'):
    classList.append(a['href'])

try:
    for url in classList:
        res = requests.get(rootUrl+url, proxies=proxy)
        innerSoup = BeautifulSoup(res.text)
        if innerSoup.findAll('img', align=None):
            MD.write('[' + url + '](' + rootUrl + url + ')\n')
            for img in innerSoup.findAll('img', align=None):
                MD.write('![' + url +'](' + rootUrl + img['src'] + ')\n')
        time.sleep(0.1)
finally:
    MD.close()

