from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card%27'
uClient=ureq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
containers=page_soup.findAll("div",{"class":"item-container"})
filename="products.csv"
f=open(filename,"w")
headers="Brand,product_name,shipping\n"
f.write(headers)
for container in containers:
    brand=container.div.div.a.img["title"]
    title_cotainer=container.findAll("a",{"class":"item-title"})
    product_name=title_cotainer[0].text
    shipping_container=container.findAll("li",{"class":"price-ship"})
    shipping=shipping_container[0].text.strip()
    print("brand:"+brand)
    f.write(brand + "," +product_name + "," + shipping + "\n")
f.close()