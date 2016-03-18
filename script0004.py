import requests
import re
import time
import os

f = open("botond_ido.txt","r")
botond_ido = int(f.read())
f.close()

if botond_ido == 0:
   os.system("./Botond_open_disable.cmd > /dev/null")
   payload = {
      'username': '',
      'password': ''
   }

   with requests.Session() as s:
      p = s.post('https://www.typingclub.com/login/', data=payload)
   r = s.get('https://www.typingclub.com/typing-qwerty-en.html')
   textToParse = r.text
   
   f = open("test.txt","a")
   f.write(textToParse)
   f.close()
   
   nm = re.search('(astar.*(> <b>(\d*)))',textToParse)
   botond_current_stars_value = int(nm.group(3))


   f = open("botond_stars.txt","r")
   botond_stars_from_file = int(f.read())
   f.close()

   if botond_current_stars_value > botond_stars_from_file:
      os.system("./Botond_open_enable.cmd > /dev/null")
      botond_ido = botond_current_stars_value - botond_stars_from_file
      f = open("botond_stars.txt","w")
      f.write(str(botond_current_stars_value))
      f.close()
      f = open("botond_ido.txt","w")
      f.write(str(botond_ido))
      f.close()
   
else:
   botond_ido = botond_ido - 1
   os.system("./Botond_open_enable.cmd > /dev/null")
   f = open("botond_ido.txt","w")
   f.write(str(botond_ido))
   f.close()

