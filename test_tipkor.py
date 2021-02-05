import requests
import bs4
import logging
import collections


def response(url:str):
    response = requests.get(url=url)

    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')

    response.encoding = 'utf-8'
    page_text = response.text

    return page_text


def page_parse (site:str):
    text = response(site)
    soup = bs4.BeautifulSoup(text, 'lxml') # объект суп
    return soup


def filter():
    x = 'class_ = '
    return

def href_find(ff):
    y = []
    soup = page_parse(ff)
    for link in soup.find_all('a'):
        x = link.get('href')
        if x is not None and x != '':
            y.append(x)
        m = set(y)
        print(m)



if __name__ == '__main__':
    site = 'https://e.mail.ru'
    href_find(site)
