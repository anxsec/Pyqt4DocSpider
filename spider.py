import time
import requests
from bs4 import BeautifulSoup


rootUrl = 'http://pyqt.sourceforge.net/Docs/PyQt4/'

proxy = {
    'http': 'http://jp.gfw.li:25'
}

i = 1
v = 0
classList = []
MD = open('README.md', 'w+')

print('Get url lsit...')
r = requests.get(rootUrl+'classes.html', proxies=proxy)
# r = requests.get(rootUrl+'classes.html')
soup = BeautifulSoup(r.text)
for a in soup.findAll('table')[1].findAll('a'):
    classList.append(a['href'])

try:
    for url in classList:
        print('Get '+str(i)+' of '+str(len(classList)))
        res = requests.get(rootUrl+url, proxies=proxy)
        innerSoup = BeautifulSoup(res.text)
        if innerSoup.findAll('img', align=None):
            print('>>>Find!')
            v += 1
            MD.write('[' + url + '](' + rootUrl + url + ')\n')
            MD.write('\n')
            for img in innerSoup.findAll('img', align=None):
                MD.write('![' + url + '](' + rootUrl + img['src'] + ')\n')
            MD.write('\n')
        else:
            print('>>>Skip...')
        time.sleep(1)
        i += 1
    print('Done!')
finally:
    MD.write('#Process done.\n#Total ' + str(len(classList)) + ' pages.\n#Get ' + str(i) + ' pages.\n#Find ' + str(v) + ' pages.')
    MD.close()

