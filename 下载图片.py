# coding:utf-8


import urllib
import urllib2

url = "http://img.ph.126.net/ocT0cPlMSiTs2BgbZ8bHFw==/631348372762626203.jpg"


# url = raw_input("url:")
# up = urllib2.urlopen(url)
# print up
# s = up.read()
# print s

urllib.urlretrieve(url,  'cz.jpg')

