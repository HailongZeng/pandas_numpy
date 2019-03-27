import os
import re

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"/Users/zenghailong/Desktop/Deep learning/prank")
    print(file_list)
    os.chdir(r"/Users/zenghailong/Desktop/Deep learning/prank")

    # (2) for each file, rename filename
    for file_name in file_list:
        a = re.findall('[a-zA-Z]+', file_name)
        new_name = ''
        for i in range(len(a)):
            if i == (len(a) - 1):
                new_name += '.' + a[i]
            else:
                new_name += ' ' + a[i]
        print(os.rename(file_name, new_name))

rename_files()