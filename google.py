import urllib2
from os.path import basename
from urlparse import urlsplit
from bs4 import BeautifulSoup

url = "http://www.naver.com"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page)

imgTags = soup.findAll('img')


for imgTag in imgTags:
	try:
		imgSrc = imgTag['data-src']
		print "download : " + imgSrc

	except:
		imgSrc = imgTag['src']
		print "download : " + imgSrc

	imgContent = urllib2.urlopen(imgSrc).read()
	imgName = basename(urlsplit(imgSrc)[2])

	save = open(imgName,'wb')
	save.write(imgContent)
	save.close()


print "Finish"
