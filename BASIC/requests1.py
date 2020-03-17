import requests
#get request: browser stores this url history
r=requests.get("")
print(r.text)

#post request: browser don't store this url history
url="www.something.com"
data={
    "p1":4,
    "p2":8
}
r2=requests.post(url=url,data=data)