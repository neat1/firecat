
from urllib.request import urlopen

from bs4 import BeautifulSoup
url = "https://www.ft.com/"
page = urlopen(url)
soup = BeautifulSoup(page,features='lxml')
page.close()




h1s = soup.find_all(class_ = "o-grid-row")
print(h1s)
for h3 in h1s:
    print(h3.a.text)



