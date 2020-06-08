#!/usr/bin/env python3
import sys

try:
    link = sys.argv[1]
    downloadLink = link.replace('file/d/', 'uc?export=download&id=')
    downloadLink = downloadLink.replace('/view?usp=sharing', '')

    print('Your URL is', downloadLink)
except:
    print('Command usage: drivedirect "[url]"')
