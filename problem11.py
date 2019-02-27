#Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.

import sys
from zipfile import ZipFile

files_list = [sys.argv[2], sys.argv[3]]
with ZipFile(sys.argv[1], 'w') as zip:
	for f in files_list:
		zip.write(f)
