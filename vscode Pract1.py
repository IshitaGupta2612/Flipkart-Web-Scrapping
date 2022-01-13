from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

offer=[]
highlight=[]

scrap_page='https://www.flipkart.com/adsun-80-cm-32-inch-hd-ready-led-smart-tv/p/itmffmnvy7khsuzx?pid=TVSFFMNVUVNS3SHF&lid=LSTTVSFFMNVUVNS3SHFVWHTAU&marketplace=FLIPKART&q=tv&store=ckf%2Fczl&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=en_bDKVa%2BRJKdg5gyiYjR0mrCLQK%2Birrb39g%2F69j7Qtbn9jrWetmNrsmZ%2B5Y1K4ZU9q6gAWckx%2BYJB4wizZEesMJQ%3D%3D&ppt=pp&ppn=pp&ssid=lmwnptn6740000001641534362402&qH=c9a1fdac6e082dd8'

fetch_url=urlopen(scrap_page)
page_html=fetch_url.read()
soup=BeautifulSoup(page_html,"html5lib")
#print(soup.prettify)

name=soup.find('span',{"class":"B_NuCI"}).text
price=soup.find('div',{"class":"_30jeq3 _16Jk6d"}).text
original=soup.find('div',{"class":"_3I9_wc _2p6lqe"}).text
NoOfRatingAndReview=soup.find('span',{"class":"_2_R_DZ"}).text
rating=soup.find('div',{"class":"_3LWZlK"}).text
delivery=soup.find('span',{"_1TPvTK"}).text
discount=soup.find('div',{"class":"_3Ay6Sb _31Dcoz"}).text
warranty=soup.find('div',{"class":"_352bdz"}).text

offers = soup.find('div', attrs={'class':'XUp0WS'})
offer.append(offers.text.strip())

highlights = soup.find('div', attrs={'class':'_2418kt'})
highlight.append(highlights.text.strip())
seller=soup.find('div',{"class":"_1RLviY"}).text

TV={'Name':name, 'Discounted Price':price,'Original Price':original, 'Discount':discount, 'Rating':rating,'No Of Ratings And Reviews':NoOfRatingAndReview, 'Delivery Time':delivery,'Warranty' : warranty, 'Offers':offer,'Highlights':highlight,'Seller':seller}
df=pd.DataFrame(TV)
print(df)
df.to_csv('FlipkartTV.csv')

