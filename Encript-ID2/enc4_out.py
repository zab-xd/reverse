# coding:utf-8
# decompile by itsuki

import os, base64, codecs
from sys import argv
from os import system
from time import ctime
import os, sys, zlib, base64, marshal, binascii, time, py_compile
from time import sleep as waktu
from random import randint
from os import system, name
os.system('clear')
version = 'JANDA MUDA '
expired = ['05', '07', '2021']
buffer_size = 898989
pesing = '\x1b[0;32m ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ \n ▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒ \n ▒▒█▒▒▒▄██████████▄▒▒▒▒ \n ▒█▐▒▒▒████████████▒▒▒▒ \n ▒▌▐▒▒██▄▀██████▀▄██▒▒▒ \n ▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒ \n ▐┼▐▒▒██████████████▒▒▒ \n ▐▄▐████─▀▐▐▀█─█─▌▐██▄▒ \n ▒▒█████──────────▐███▌ \n ▒▒█▀▀██▄█─▄───▐─▄███▀▒ \n ▒▒█▒▒███████▄██████▒▒▒ \n ▒▒▒▒▒██████████████▒▒▒ \n ▒▒▒▒▒██████████████▒▒▒ \n ▒▒▒▒▒█████████▐▌██▌▒▒▒ \n ▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒ \n ▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒ \n ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ \n\n     \x1b[0;31m╔════•ೋೋ•════╗  \n     \x1b[0;37m☆ۣۜۜ͜͡₲ℜ❍Ⴎℙ B!it@r♤ \n     \x1b[0;31m╚════•ೋೋ•════╝ \n'
'Jngan Di recode Hargai Karya Org'
'Klu Di Bongkar Pakek Sendiri/Jangan Di Jual Belikan'
'Selalu Bijak Dalam Segala Hal'
"Tentunya Tidak Merugikan Org Laen *4"

def kontol(ngaceng):
    for peli in ngaceng + '\n':
        sys.stdout.write(peli)
        sys.stdout.flush()
        time.sleep(random.random() * 0.0001)
        
sys.stdout.write('\x1b[1;35m\x1b]2; ✧ @ ENCRIPT PYTHON OBFUSCATE ✧ \x07')
 

def login():
    os.system('clear')
    from datetime import datetime
    saat_ini = datetime.now()
    tgl = saat_ini.strftime('%d')
    bln = saat_ini.strftime('%m')
    thn = saat_ini.strftime('%Y')
    tanggal = thn + bln + tgl
    exp = expired[2] + expired[1] + expired[0]
    if tanggal >= exp:
        print (('\n').join(['' + pesing + '']))
        print (('\n').join(['\x1b[1;31m ➤ \x1b[1;33mSCRIPT KADALUWARSA MBAH.. 😊\n\x1b[1;31m ➤ \x1b[1;32mAYUK HUBUNGI AUTORNYA \n \x1b[1;31m➤ \x1b[1;35mJANGAN LUPA DONASI SEIKHLASNYA 🐧 \n \x1b[1;31m➤ \x1b[1;36mSILAHKAN CEK YT ARIS SETYA CHANNEL \n \x1b[1;31m➤ \x1b[1;37mDI SUBSCRIBE YA SAYANG (☉‿☉✿)']))
        sys.exit()
    else:
        main()
        
note = '\n# Obfuscated By Arya77\n'
flag1 = ctime()
flag2 = os.uname()
flag3 = '# Time      : ' + flag1 + '\n'
flag4 = '# Platform  : ' + flag2[0] + ' ' + flag2[4] + '\n'
flag0 = '#################\n'
obf_note = note + flag0 + flag3 + flag4 + flag0

def main(file):
    try:
        htr1 = open(file).read()
    except IOError:
        os.sys.exit('\033[1;31m Tak ada File')

    htr2 = file.replace('.py', '_hasil.py')
    htr3 = base64.b64encode(htr1)
    h1 = []
    h2 = []
    h3 = []
    h4 = ''
    h5 = ''
    for x in htr3:
        h1.append(ord(x))

    z = 0
    while 1:
        h2.append(h1[z])
        if z >= len(h1) / 2:
            break
        z += 1

    v = len(h1) / 2 + 1
    try:
        while 1:
            h3.append(h1[v])
            v += 1

    except IndexError:
        pass

    for s in h3:
        h4 += chr(s)

    htr4 = codecs.encode(h4, 'rot_13')
    h6 = open(htr2, 'w')
    h6.write(obf_note + '\nimport codecs,base64\n' + 'htr = ' + str(h2) + '\t\t\n' + "tahmid = '" + str(htr4) + "'\t\t\n")
    h6.write("pizza = '\\x72\\x6f\\x74\\x5f\\x31\\x33'\t\t\n")
    h6.write("mobile = codecs.decode(eval('\\x74\\x61\\x68\\x6d\\x69\\x64'), eval('\\x70\\x69\\x7a\\x7a\\x61'))\t\t\n")
    h6.write("burger = base64.b64decode(''.join([chr(tech) for tech in htr])+eval('\\x6d\\x6f\\x62\\x69\\x6c\\x65'))\t\t\n")
    h6.write('eval(compile(eval("\\x62\\x75\\x72\\x67\\x65\\x72"),"<arya77>","exec"))\t\t\n')
    h6.close()
    print '\n\033[1;32m > Berhasil Di encrypt ' + htr    
    
    
if __name__ == '__main__':
    if len(argv) >= 2:
        main(argv[1])
    else:
        os.sys.exit('\n\033[1;33m Caranya : ' + __file__ + ' <script>')

