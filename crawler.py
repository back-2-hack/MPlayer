import os
import sys
from os import path

temp_files = []
files = []

class bcrawler:
    def crawl(target_dir):
        target_dir = target_dir
        for i in os.walk(target_dir):
            temp_files.append(list(i))
        
        for i in temp_files:
            for j in i[-1]:
                files.append(i[0]+'/'+j)
        return files
