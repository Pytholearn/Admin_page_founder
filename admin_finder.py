from requests import get

site = input("Enter a Target Site URL : ")
site = "http://"+site
Urls = input("Enter a Urls File : ")

Urls = open(Urls,"r").read().splitlines()

for url in Urls:
    full_address = site+"/"+url
    respons = get(full_address)
    if respons.status_code == 200:
        print(f"{full_address} is OK => 200")
    else:
        print(f"{full_address} is not True => 400")