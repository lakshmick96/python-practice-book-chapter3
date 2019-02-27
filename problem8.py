import urllib
import re
import string

url = "http://pramode.net/"
r = urllib.urlopen(url)
s = r.read()
for i in s.split():
	if re.search('href="http', i):
		i = string.strip(i, 'href=')
		print i.split('>')[0]

print s.split('<','>')

