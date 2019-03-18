import requests
from bs4 import BeautifulSoup
# from .models import Autopost

def testautocrawl(siteurl, url, selection, gettag):
    print("=====================================")
    headers={
        'Referer' : url,
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    req = requests.get(url, headers=headers)
    html = req.text
    
    soup = BeautifulSoup(html, 'html.parser')
    print(selection)
  
    data=[]
    my_titles = soup.select( selection )

    for title in my_titles:
        real_link_type=title.get(gettag)
        real_link=str(real_link_type)
        i=real_link.find(siteurl)
        if i==-1:
            data.append(siteurl+real_link)
            print(real_link)
        else:
            data.append(real_link)

    # for link in sel_data:
    #     title = link.string
    #     real_link=link.get(gettag)
    #     subject[title]=real_link
    
    # findall 방식
    # divs =soup.findall('div', {})
    # for div in divs:
    #     links=div.findall('a')
    #     for link in links:
    #         subject = link.text
    #         subjects.append(subject)
    
    return data
def autocrawl(url, selection, gettag):
 
    data = []
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    
    # my_titles = soup.select(
    #     "meta[property='og:title']"
    #     )
    my_titles = soup.select(
        selection
        )
    # print(my_titles)
    
    
    # my_titles는 list 객체
    for title in my_titles:
        print(title.get('content'))
        # data[title.text] = title.get('content')
    return title.get(gettag)