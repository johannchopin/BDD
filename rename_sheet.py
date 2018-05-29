from os import listdir, rename
from urllib.request import unquote

files = listdir()
files.remove('rename_sheet.py')

for name in files:
    print(unquote(name[:4])) # Check if all works, then use rename in comment
    #rename(name, unquote(name[:4]))