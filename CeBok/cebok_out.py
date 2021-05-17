# Decompile By Itsuki ft. Aap Afandi ID
"""
#################################
###   DILARANG KERAS COMLI!   ###
###   SANGE KOK SAMA CERITA   ###
### CUMA NGETES SKILL PARSING ###
#################################
"""
__credit__ = ['CritaSex.live','ZurstX7','UC Browser (buat nyari webnya)']
import os, time, sys
try:
	import requests
except ImportError:
	os.system('python3 -m pip install -q requests')
	import requests
try:
	from bs4 import BeautifulSoup as soup
except ImportError:
	os.system('python3 -m pip install -q bs4')
	from bs4 import BeautifulSoup as soup

class Sange:
	def __init__(self):
		os.system('clear')
		self.main_url = 'http://207.7.81.200/'
		self.url = self.main_url
		self.page = 1
		self.logo = '\n    ╔═╗┌─┐╔╗ ┌─┐┬┌─\n    ║  ├┤ ╠╩╗│ │├┴┐\n    ╚═╝└─┘╚═╝└─┘┴ ┴\n[ Cerita Bokep Online ]\n[    IG : @zurstx_    ]\n'
		self.last = 0
		self.judul = []
		self.link = []
		self.gas()

	def get_data(self, url):
		try:
			html = soup(requests.get(url).text,'html.parser')
		except:
			exit("[!] Ada yang error cuk, coba cek jaringan")
		data = html.find('div', id='content')
		jatah = data.findAll('a', rel='bookmark')
		self.judul = list(dict.fromkeys([_['title'] for _ in jatah]))
		self.link = list(dict.fromkeys([_['href'] for _ in jatah]))
		self.last = 60

	def gas(self):
		while True:
			os.system('clear')
			print (self.logo)
			print ("="*30)
			print ("| N untuk ke halaman berikutnya")
			print ("| P untuk ke halaman sebelumnya")
			print ("| E untuk keluar")
			print ("| Ketik |** untuk lompat ke halaman tersebut")
			print ("| Ganti ** jadi angka yang ingin dituju")
			print ("="*30)
			self.get_data(self.url)
			hm = 0
			for ___ in self.judul:
				print (f'({str(hm)}) {___}')
				hm +=1
			cus = str(input(f"({str(self.page)}/{str(self.last)})>>> ")).upper()
			if cus.isdigit():
				if int(cus) >= len(self.judul):
					print ("[!] Kelebihan goblok")
				else:
					self.read(self.link[int(cus)])
			else:
				if cus == "P":
					if self.page == 1:
						print ("[*] Mentok awal woy")
					else:
						self.page -=1
						self.url = (self.main_url + 'page/' + str(self.page))
				elif cus == "N":
					if self.page == self.last:
						print ("[*] Mentok akhir woy")
					else:
						self.page +=1
						self.url = (self.main_url + 'page/' + str(self.page))
				elif cus.startswith("|"):
					yup = int(cus.replace('|',''))
					if yup >= self.last+1:
						print ("[!] Kelebihan goblok")
					elif yup <= 0:
						print ("[!] Mentok awal woy")
					elif yup == self.page:
						print ("[!] Ini udah disini woy")
					else:
						self.page = yup
						self.url = (self.main_url + 'page/' + str(yup))
				else:
					exit("[*] Oke keluar, jan lupa follow ig gw ya")
			time.sleep(1)

	def read(self, link):
		try:
			data = soup(requests.get(link).text, 'html.parser')
		except:
			exit("[!] Ada yang error")
		capt = data.findAll('p')[:-5]

		# Sorting blank text
		##############
		ion = []
		for _ in capt:
			if _.text:
				ion.append(_.text)
		##############

		print ("\n[*] Jika belum tamat klik enter untuk melanjutkan membaca")
		print ("[*] Ketik 'cukup' untuk menyelesaikan membaca")
		print ('='*55)
		q = 1
		for y in ion:
			self.outp (y)
			___ = input(f"({str(q)}/{str(len(ion))}) ")
			if str(___).lower() == 'cukup': break
			q +=1
		input("[!] Udah tamat\n[*] Enter buat kembali")
		del ion
		self.gas()

	def outp(self, text):
		for x in (text + '\n'):
			sys.stdout.write(x)
			sys.stdout.flush()
			time.sleep(0.003)
try:
	Sange()
except KeyboardInterrupt:
	exit("[*] Oke keluar, jan lupa follow ig gw ya!")


