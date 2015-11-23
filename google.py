import urllib2
from os.path import basename
from urlparse import urlsplit

from bs4 import BeautifulSoup


def extract():
    for img_tag in img_tags:
        try:
            img_src = img_tag['data-src']
            print "download : " + img_src

        except:
            img_src = img_tag['src']
            print "download : " + img_src

        img_content = urllib2.urlopen(img_src).read()
        img_name = basename(urlsplit(img_src)[2])

        with open(img_name,'wb') as _file:
            _file.write(img_content)

if __name__ == '__main__':
    url = "http://www.naver.com"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    img_tags = soup.findAll('img')
    extract(img_tags)

    print "Finish"

