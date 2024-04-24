import requests
import pandas as pd
from bs4 import BeautifulSoup

#response=request.get("url")
#output should be in 200 i.e success to scrap data


url="https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
print(soup.text)

names=soup.find_all('div', class_="_4rR01T" )
name=[]
for i in names[0:10]:
    k=i.get_text()
    name.append(k)
print(name)

prices=soup.find_all('div', class_="_30jeq3 _1_WHN1")
price=[]
for j in prices[0:10]:
    n=j.get_text()
    price.append(n)
print(price)    

ratings=soup.find_all('div', class_="_3LWZlK")
rate=[]
for a in ratings[0:10]:
    m=a.get_text()
    rate.append(float(m))
print(rate)    

images=soup.find_all('img' ,class_="_396cs4" )
image=[]
for b in images[0:10]:
    o=b['src']
    image.append(o)
print(image)    


links=soup.find_all('a',class_="_1fQZEK")
link=[]
for c in links[0:10]:
    d="https://www.flipkart.com/"+c['href']
    link.append(d)
print(link)    

df=pd.DataFrame()
df["Name"]=name
df["Prices"]=price
df["Ratings"]=rate
df["Images"]=image
df["Links"]=link
df.to_csv("Mobiles.csv")
