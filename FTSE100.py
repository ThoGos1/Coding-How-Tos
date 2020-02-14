import requests
from bs4 import BeautifulSoup



URL = 'https://www.bbc.co.uk/news/topics/c9qdqqkgz27t/ftse-100'

page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')
price =  soup.find('div', attrs={'class':'gel-paragon nw-c-md-market-summary__value'})


print(price.text)
