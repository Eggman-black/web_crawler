import requests
from bs4 import BeautifulSoup	
import os
import shutil
num=0
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
tar = 'https://memes.tw/wtf?page='
folder_path = 'webmemes\\'
keyword = input('關鍵字?(無則寫none)')
if(keyword != 'none'):
    folder_path = 'webmemes_'+keyword+'\\'
    tar = 'https://memes.tw/wtf?q='+keyword+'&page='
req = requests.get(url = tar+'1', headers=header)
bs = BeautifulSoup(req.text,"html.parser")
pagelink = bs.find_all('a', class_='page-link')
print(pagelink)

pagecnt = 1
for link in pagelink:
    #print(link)
    #print(link.string)
    if not link.string in ['›', '‹']:
        pagecnt = max(int(link.string), pagecnt)
    #print(link["string"])
print('共有',pagecnt,'頁')
n = int(input("要爬幾頁?"))
while(n>pagecnt):
    n = int(input("不要超過所有頁數!!!請重新輸入"))
f = int(input('從第幾頁開始?'))



if os.path.exists(folder_path):
	shutil.rmtree(folder_path)
else:
	os.makedirs(folder_path)
for con in range(f, n+f+1):
    print('第',con,'頁')
    page = str(con)
    target = tar+page
    req = requests.get(url = target, headers=header)
    bs = BeautifulSoup(req.text,"html.parser") #將網頁資料以html.parser
    links = bs.find_all('div','sensitive-content')#抓圖片的部分html
    
    for i in links:
        #print(s.prettify())0++
        if i.find('a') != None:
            href = 'https://memes.tw'+i.a['href']
            #print(href)
            req = requests.get(url=href,headers=header)
            bs = BeautifulSoup(req.text,'html.parser')
            if bs.find('div','text-center mb-2').img != None:
                num += 1
                src = bs.find('div','text-center mb-2').img['src']
                print(src)
                img_byte = requests.get(src).content
                file = open(folder_path+str(num)+'.jpg','wb')
                file.write(img_byte)
                file.close()
                print('第'+str(num)+'張下載完成')