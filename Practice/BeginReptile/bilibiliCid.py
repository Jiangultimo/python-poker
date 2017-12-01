import requests
import bs4
import re

aid = input('请输入AV号，如果多个，请使用\',\'隔开:')
aids = re.split(',', aid) # 列表化

links = []
for id in aids:
    links.append("http://www.bilibili.com/video/av"+id+"/")

for link in links:
    oid = int(re.findall('\d+', link)[0])
    r = requests.get(link)
    '''https://www.bilibili.com/blackboard/html5player.html?aid=3521416&cid=6041635'''
    r.encoding = r.apparent_encoding
    soup = bs4.BeautifulSoup(r.text,'lxml')
    print('------------------------------')
    for script in soup.find_all('script', src=False):
        if re.search('cid', script.get_text()) != None:
            ids = re.split(',', script.get_text())[len(re.split(',', script.get_text())) - 1].split('&')
            cid = int(re.findall('\d+', ids[0])[0])
            print(link + ' cid is:', cid)
            # print("html5:https://www.bilibili.com/blackboard/html5player.html?aid="+oid+"&cid="+cid)
            print(oid,cid)
            print("https://www.bilibili.com/blackboard/html5player.html?aid="+str(oid)+"&cid="+str(cid))

