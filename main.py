import time
import random
import colorama
from colorama import Fore, Style
import nmap 

na = nmap.PortScanner()
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
reset = Style.RESET_ALL
def menu():
    print (blue + "=================================================")
    print ("=================================================")
    print (Style.RESET_ALL)
    print (green + "WELCOME :D  ")
    print (" ") 
    print ("=================================================")
    print ("=================================================")
    print (reset)
     

menu()
print ("Made by ps : email me at pshacker@protonmail.com :> Happy Hacking ! ") 
time.sleep(1)

website = input("1)What do we have to hack today ? !!!!! put the IP NOT url !!!!! >  ")
print ("Today we hack : " + website )
print ("2)Now you have to chose what type of scan you want ! ")
print (blue + "1 - Casual , we do a quick scan , about 1000 ports scanned ")
print (reset)
print (green + "2 - Intense , we do a full 10.000 port scan , it may take a while ")
print (reset)
chose_1 = int(input("What will it be ? > "))
if chose_1 == 1 :
    print ("Getting website ...")
    time.sleep(1)
    print ("Version of nmap : " )
    print (na.nmap_version())
    print ("Starting light scan ")
    na.scan(website, '1-1024', '-v')
    print(na.scaninfo())
    print (na.csv())

if chose_1 == 2 :
    print ("Getting some stuff done ... ")
    time.sleep(1)
    na.scan(website, '1-10000','-v --version-all')
    print(na.scanstats())
    print(na[website].all_protocols)
    print (na.scaninfo())
print ("Thanks and hack the  WORLD !!!")



