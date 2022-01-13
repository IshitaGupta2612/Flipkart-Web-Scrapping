from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

name=[]             
price=[]              
original=[]
rating=[]            
NoOfRatingsAndReviews=[]              
discount=[]

features=[]
scrap_page='https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

fetch_url=urlopen(scrap_page)
page_html=fetch_url.read()
soup=BeautifulSoup(page_html,'html5lib')

details=soup.findAll('div',class_='_3pLy-c row')
for i in details:
        name.append(i.find('div',{'class':'_4rR01T'}).text)
        price.append(i.find('div',{'class':'_30jeq3 _1_WHN1'}).text)
        original.append(i.find('div',{'class':'_3I9_wc _27UcVY'}).text)
        discount.append(soup.find('div',{"class":"_3Ay6Sb"}).text.strip())
        rating.append(i.find('div',{'class':'_3LWZlK'}).text) 
        NoOfRatingsAndReviews.append(i.find('span',{'class':'_2_R_DZ'}).text) 
        features.append(i.find('div',{'class':'fMghEO'}).text.strip())

df=pd.DataFrame({'Name':name,'Discounted Price':price,'Original Price':original,'Discount':discount,'Rating':rating,'No Of rating And Reviews':NoOfRatingsAndReviews,'features':features})
print(df)
df.to_csv('TVs.csv')

