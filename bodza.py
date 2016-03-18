import requests
import re
import os

f = open("bodza_ido.txt","r")
bodza_ido = int(f.read())
f.close()

payload = {
   'username': '',
   'password': ''
}

with requests.Session() as s:
   p = s.post('https://www.typingclub.com/login/', data=payload)
r = s.get('https://www.typingclub.com/typing-qwerty-en.html')
textToParse = r.text

nm = re.search('(astar.*(> <b>(\d*)))',textToParse)
bodza_current_stars_value = int(nm.group(3))

f = open("bodza_stars.txt","r")
bodza_stars_from_file = int(f.read())
f.close()


if bodza_current_stars_value > bodza_stars_from_file:
   os.system("./Bodza_open_enable.cmd > /dev/null")
   os.system("./Papa_open_enable.cmd > /dev/null")
   bodza_ido = bodza_ido + 10 * (bodza_current_stars_value - bodza_stars_from_file)
   f = open("bodza_stars.txt","w")
   f.write(str(bodza_current_stars_value))
   f.close()
   f = open("bodza_ido.txt","w")
   f.write(str(bodza_ido))
   f.close()
   # felírjuk a webre is az új időt
   f = open("/var/www/html/bodza.html","w")
   f.write(str(bodza_ido))
   f.close()


if bodza_ido == 0:
   os.system("./Bodza_open_disable.cmd > /dev/null")
   os.system("./Papa_open_disable.cmd > /dev/null")

   
else:
   bodza_ido = bodza_ido - 1
   os.system("./Bodza_open_enable.cmd > /dev/null")
   os.system("./Papa_open_enable.cmd > /dev/null")
   f = open("bodza_ido.txt","w")
   f.write(str(bodza_ido))
   f.close()
   # felírjuk a webre is az új időt
   f = open("/var/www/html/bodza.html","w")
   f.write(str(bodza_ido))
   f.close()
