import os,time,sys,shutil
import os 
import sys

os.system("clear")
os.system("termux-open-url   https://youtube.com/channel/UC2ItJzPgWyihgREWErfr65g ")

class Main:
  
	def __init__(self):
		self.detekos()

	def menu(self):
		print(""" ══╦╗────╔╗─╔╗╔╗
╚╗╔╣╚╦═╦═╣╚╗║╚╝╠═╦╦╗
─║║║║║╬║║║╩║╚╗╔╣║║║║
─╚╝╚╩╩╩╩╩╩╩╝─╚╝╚═╩═╝\033[1;32m𝙎𝙋𝘼𝙈 𝙐𝙉𝙇𝙄𝙈𝙄𝙏𝙀𝘿
]────────────||────────────────[
\033[1;32mAUTHOR  \033[1;31m :\033[1;0m MAHENDRA
\033[1;32mYOUTUBE \033[1;31m : \033[1;0mTUTORIAL UTAMA
]────────────||────────────────[
───────────────|\033[1;32m𝘗𝘌𝘕𝘎𝘎𝘜𝘕𝘈:\033[1;31m5 𝘖𝘙𝘈𝘕𝘎   
                𝘙𝘈𝘛𝘐𝘕𝘎𝘚 : ★★★
\033[1;35m1.𝙋𝘼𝙔𝙁𝘼𝙕𝙕      ──────────────────
2.𝙃𝘼𝙇𝗢𝘿𝙊𝙊𝙆
3.𝙃𝙐𝘽𝙐𝙉𝙂𝙄 𝘼𝙐𝙏𝙃𝙊𝙍(𝘑𝘐𝘒𝘈 𝘚𝘊𝘙𝘐𝘗𝘛 𝘌𝘙𝘙𝘖𝘙)         
───────────────|
\033[1;31m 𝘑𝘈𝘕𝘎𝘈𝘕 𝘓𝘜𝘗𝘈 𝘚𝘜𝘉𝘚𝘊𝘙𝘐𝘉𝘌 𝘠𝘛 𝘈𝘐𝘕𝘎:) 
|||||||||||||||||||||||||||||||||||||||||||


""")
		pilih=int(input('𝙀𝙉𝙏𝙀𝙍 '))
		if pilih == 1:
			import src.payu
		elif pilih == 2:
			import src.alodok
		elif pilih == 3:
			import src.wa
	
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
