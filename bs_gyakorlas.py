from urllib.request import urlopen
from bs4 import BeautifulSoup

with open("ecologicalpyramid.html","r") as ecological_pyramid:
     soup = BeautifulSoup(ecological_pyramid,"lxml")
producer_entries = soup.find("ul")
#print(producer_entries.li.div.string)
#print(producer_entries)
#print(producer_entries.li)

