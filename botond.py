# 2016-03-17 12:03:17 Budapest Time: 
# botond.py


import requests
import re
import os

# megnézzük, hogy hány perce van még
f = open("botond_ido.txt","r")
botond_ido = int(f.read())
f.close()

payload = {
   'username': '',
   'password': ''
}
# beloggolounk
with requests.Session() as s:
   p = s.post('https://www.typingclub.com/login/', data=payload)

# lekérjük a főoldalt, ahol a csillagok számát mutatják
r = s.get('https://www.typingclub.com/typing-qwerty-en.html')
textToParse = r.text

# megkeressük a csillagok számát regexpel és letároljuk
nm = re.search('(astar.*(> <b>(\d*)))',textToParse)
botond_current_stars_value = int(nm.group(3))

# kiolvassuk az eddig megszerzett csillagok számát
f = open("botond_stars.txt","r")
botond_stars_from_file = int(f.read())
f.close()

if botond_current_stars_value > botond_stars_from_file:

   # nyitjuk a netet
   os.system("./Botond_open_enable.cmd > /dev/null")

   # minden megszerzett csillagért 5 percet kap
   botond_ido = botond_ido + 5 * (botond_current_stars_value - botond_stars_from_file)

   # felírjuk a csillagokat
   f = open("botond_stars.txt","w")
   f.write(str(botond_current_stars_value))
   f.close()

   # felírjuk az új időt
   f = open("botond_ido.txt","w")
   f.write(str(botond_ido))
   f.close()

   # felírjuk a webre az új időt
   f = open("/var/www/html/botond.html","w")
   f.write(str(botond_ido))
   f.close()
   

   



# ha már nincs egy se, akkor zárjuk a netet
if botond_ido == 0:
   os.system("./Botond_open_disable.cmd > /dev/null")

   # megnézzük, hogy van-e újabb csillaga
   # ez itt a felhasználónév / jelszó

   # összehasonlítjuk a mostani és az eddig megszerzett csillagokat.
   # ha több lett, akkor nyitjuk a netet
# ha van még ideje
else:
   # akkor leveszünk belőle egy percet
   botond_ido = botond_ido - 1
   # nyitjuk a netet (biztos, ami biztos)
   os.system("./Botond_open_enable.cmd > /dev/null")
   # mentjük az új időt
   f = open("botond_ido.txt","w")
   f.write(str(botond_ido))
   f.close()
   # felírjuk a webre is az új időt
   f = open("/var/www/html/botond.html","w")
   f.write(str(botond_ido))
   f.close()
