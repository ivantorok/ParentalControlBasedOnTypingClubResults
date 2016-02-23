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
f = open("test.txt","w") #opens file with name of "test.txt"
f.write(r.text)
f.close()
import re
m = re.search('(?<=, "score"..)(\d*)(?=, "stars"..)',textToParse)
print (m.group(0))
