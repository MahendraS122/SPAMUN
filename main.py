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
─╚╝╚╩╩╩╩╩╩╩╝─╚╝╚═╩═╝\033[1;32mSPAM
UNLIMITED
]────────────||────────────────[
\033[1;32mAUTHOR  \033[1;31m :\033[1;0m MAHENDRA
\033[1;32mYOUTUBE \033[1;31m : \033[1;0mTUTORIAL UTAMA
]────────────||────────────────[
───────────────|\033[1;32mPENGGUNA:\033[1;31m150 ORANG   
                RATINGS : ★★★
\033[1;35m1.PAYFAZZ      ──────────────────
2.HALODOK
3.HUBUNGI AUTHOR (JIKA SCRIPT ERROR)         
───────────────|
\033[1;31m JANGAN LUPA SUBSCRIBE YT AING:) 
|||||||||||||||||||||||||||||||||||||||||||


""")
		pilih=int(input('ENTER '))
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
