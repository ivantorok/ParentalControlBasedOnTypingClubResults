import requests

# Fill in your details here to be posted to the login form.
payload = {
    'username': 'b611742@trbvn.com',
    'password': 'b611742@trbvn.comb611742@trbvn.com'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('https://www.typingclub.com/login/', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.

    # An authorised request.
r = s.get('https://www.typingclub.com/typing-qwerty-en.html')
textToParse = r.text
import re
m = re.search('(?<=, "score"..)(\d*)',textToParse)
current_score_value = m.group(0) + '\n' 
nm = re.search('(?<=, "stars"..)(\d*)',textToParse)
current_stars_value = nm.group(0) + '\n'
f = open("test.txt","w") #opens file with name of "test.txt"
f.write(current_score_value)
f.write(current_stars_value)

f.close()

