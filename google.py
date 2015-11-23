from os.path import basename
from urlparse import urlsplit

import requests
from bs4 import BeautifulSoup


def extract(html):
    soup = BeautifulSoup(html)
    img_tags = soup.findAll('img')

    for img_tag in img_tags:
        try:
            img_src = img_tag['data-src']
            print "download : " + img_src

        except:
            img_src = img_tag['src']
            print "download : " + img_src

        img_content = requests.get(img_src).content
        img_name = basename(urlsplit(img_src)[2])

        with open(img_name,'wb') as _file:
            _file.write(img_content)


def get_html(url):
    return requests.get(url).content


if __name__ == '__main__':
    extract(get_html('http://naver.com'))
    print "Finish"

