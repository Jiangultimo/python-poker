import requests
import bs4
import re

r = requests.get("http://www.bilibili.com/video/av16735209/")
'''https://www.bilibili.com/blackboard/html5player.html?aid=3521416&cid=6041635'''
r.encoding = r.apparent_encoding
soup = bs4.BeautifulSoup(r.text,'lxml')
print('------------------------------')
scripts = []
for script in soup.find_all('script', src=False):
    # print(re.search('cid', script.get_text()))
    if re.search('cid', script.get_text()) != None:
        print(re.split(',',script.get_text()))
