import requests
from bs4 import BeautifulSoup
from .models import Autopost

def testautocrawl(url, selection, gettag):
    data = []
    headers={
        'Referer' : url,
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    html = requests.get(url, headers=headers).text
    # html = req.text
    
    soup = BeautifulSoup(html, 'html.parser')
    print(selection)
    subjects=[]
    # sel_data = soup.select(
    #         selection
    #         )
    # divs =soup.findall('div', {})
    # for div in divs:
    #     links=div.findall('a')
    #     for link in links:
    #         subject = link.text
    #         subjects.append(subject)
    return html

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