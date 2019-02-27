#Write a program to list all the files in the given directory along with their length and last modification time. 
#The output should contain one line for each file containing filename, length and modification date separated by tabs.

from os import *
def files_list(folder):
    files = [f for f in listdir(folder) if path.isfile(path.join(folder, f))]
    for i in files:
        status = stat(path.join(folder, f))
        print i, status.st_size, status.st_mtime

folder = '/home/lakshmi/Downloads/recursive/c'
files_list(folder)

    
