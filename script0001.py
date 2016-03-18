import requests
import re
mport time


payload = {
    'username': 'b611742@trbvn.com',
    'password': 'b611742@trbvn.comb611742@trbvn.com'
}

with requests.Session() as s:
    p = s.post('https://www.typingclub.com/login/', data=payload)
r = s.get('https://www.typingclub.com/typing-qwerty-en.html')
textToParse = r.text

m = re.search('(?<=, "score"..)(\d*)',textToParse)
current_score_value = m.group(0) + ' ' 
nm = re.search('(?<=, "stars"..)(\d*)',textToParse)
current_stars_value = nm.group(0)

DateTimeStamp = '\n' + time.strftime("%Y-%m-%d %X ")


f = open("test.txt","a") #opens file with name of "test.txt"
f.write(DateTimeStamp)
f.write(current_score_value)
f.write(current_stars_value)

f.close()

