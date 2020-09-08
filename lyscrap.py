from bs4 import BeautifulSoup
import requests
s=[]
b=[]
artist1=""
song1=""
song=input("Enter the name of your favourite song\n")
for item in song:
    if item.isupper():
        s.append(item.lower())
    elif item==" ":
        s.append("-")
    else:
        s.append(item)
for item in s:
    song1+=item
artist=input("Enter the artist\n")
for item in artist:
    if item==" ":
        b.append("-")
    else:
        b.append(item)
b[0]=b[0].upper()
for item in b:
    artist1+=item
print("https://genius.com/"+artist1+"-"+song1+"-lyrics")
res=requests.get("https://genius.com/"+artist1+"-"+song1+"-lyrics")
bs=BeautifulSoup(res.text,'lxml')
a=[]
for item in bs.p.text:
    a.append(item)
for item in a:
    print(item,end="")
