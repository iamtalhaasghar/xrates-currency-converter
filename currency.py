from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

url = 'https://www.x-rates.com/calculator/?from=USD&to=PKR&amount=1'
site = urlopen(url)
data = bs(site.read(), 'lxml')
result = data.find(class_="ccOutputRslt")
print(result.text)
