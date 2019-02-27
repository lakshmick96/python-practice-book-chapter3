#Create a new virtualenv and install BeautifulSoup. BeautifulSoup is very good library for parsing HTML. Try using it to extract all HTML links from a webpage.

from bs4 import BeautifulSoup
import urllib2
url = "http://pramode.net/"
c = urllib2.urlopen(url).read()
s = BeautifulSoup(c)
for i in s.find_all('a'):
    print(i.get("href"))
