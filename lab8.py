import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.forever21.com/us/shop/catalog/category/f21/women-new-arrivals-clothing?cgid=women_new_arrivals_clothing&sz=30").content
soup = BeautifulSoup(data, 'html.parser')

#getting the title of clothes
p = soup.find("p", {"class":"product-tile__body-section product-tile__name text-line--small letter-spacing--small body-type--centi"})

#getting the price of clothes
span = soup.find("div", {"class":"body-type--deci text-line--large product-tile__price-container"})

title = p.string.strip()
price = span.getText().strip()

print("Item and price:", title, price)