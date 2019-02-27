#Write a program to list all files in the given directory.

import os

def files_list(folder):    
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    return files

folder = '/home/lakshmi'
print files_list(folder)


