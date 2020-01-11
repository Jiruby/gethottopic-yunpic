from bs4 import BeautifulSoup
import requests
import pandas as pd
import chardet
import numpy as np



'''
creat beautifulsoup
'''
def creat_bs(url):
    result = requests.get(url)
    e=chardet.detect(result.content)['encoding']
    #set the code of request object to the webpage's code
    result.encoding=e
    c = result.content
    soup=BeautifulSoup(c,'lxml')
    return soup


'''
build urls group
'''
def build_urls(prefix,suffix):
    urls=[]
    for item in suffix:
        url=prefix+item
        urls.append(url)
    return urls


'''
acquire all the page titles and links and save it
'''
def find_title_link(soup):
    titles=[]
    try:
        contanier_0=soup.find('body',{'id':'nv_forum'})
        contanier_1=contanier_0.find('div',{'id':'comiis_topbg'})
        print('ok contanier_1')
        contanier_2=contanier_1.find('div',{'id':'wp'})
        contanier_3=contanier_2.find('div',{'class':'boardnav'})
        threadlist=contanier_3.find('div',{'id':'threadlist'})
        bm_c=threadlist.find('div',{'class':'bm_c'})
        table_=bm_c.find('table',{'cellspacing':0})
        page_list=table_.find_all('tbody')
        for page in page_list:
            titlelink_th=page.find('th',{'class':'common'})
            titlelink=titlelink_th.find('a',{'class':'xst'})
            if titlelink.text==None:
                title=titlelink.find('b').text
            else:
                title=titlelink.text
            titles.append(title)
    except:
        print('have none value')
    return titles

'''
acquire information from hupu pubg bbs
'''
url='http://www.jmbbs.com/forum.php?mod=guide&view=new&page='
page_suffix=['','2','3','4','5','6','7','8','9','10']
urls=build_urls(url,page_suffix)


title_group=[]
for url in urls:
    soup=creat_bs(url)
    titles=find_title_link(soup)
    for title in titles:
        title_group.append(title)

'''
creat wordlist and save as txt
'''
wordlist=str()
for title in title_group:
    wordlist+=title  #+'\n'

def savetxt(wordlist):
    f=open('wordlist.txt','wb')
    f.write(wordlist.encode('utf8'))
    f.close()
savetxt(wordlist)


