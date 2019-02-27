#Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.

import sys

mod = sys.argv[1]
import (mod)
help(mod)

