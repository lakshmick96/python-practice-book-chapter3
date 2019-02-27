# Write a program extcount.py to count number of files for each extension in the given directory. 
#The program should take a directory name as argument and print count and extension for each available file extension.

import sys
from os import *

d = sys.argv[1]
e = {}
for f in listdir(d):
    if path.isfile(path.join(d, f)):
        g = f.split('.')
        if len(g) == 2:
            e[g[1]] = e.get(g[1], 0) + 1
for i in e:
    print e[i], i

            
        
