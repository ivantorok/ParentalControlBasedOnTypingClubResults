# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('192.168.1.2',)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print (p.text)
