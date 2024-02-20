import mrequests

host = 'http://httpbin.org/'
#host = "http://localhost/"
url = host + "get"
r = mrequests.get(url, headers={b"Accept": b"application/json"})
print(r)

if r.status_code == 200:
    print(r.content)
    print(r.text)
    print(r.json())
else:
    print("Request failed. Status: {}".format(r.status_code))

r.close()
