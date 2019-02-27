#Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.

import urllib
import sys

url = sys.argv[1]
if url.split('/')[-1] == '':
    file_name = 'index.html'
else:
    file_name = url.split('/')[-1]

u = urllib.urlopen(url)
f = open(file_name, 'w')

f.write(u.read())
f.close()
print('saving %s as %s.' %(url, file_name))
