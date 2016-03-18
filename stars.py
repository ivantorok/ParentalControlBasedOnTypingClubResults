path = "./"
path2 = "/var/www/html/stars.html"



f = open(path + "bodza_ido.txt", "r")
szoveg = f.read()
f.close()

f = open(path + "botond_ido.txt", "r")
szoveg = szoveg + " " + f.read()
f.close()

f = open(path2, "w")
f.write(szoveg)
f.close
