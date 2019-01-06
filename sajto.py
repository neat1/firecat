from urllib.request import urlopen

from bs4 import BeautifulSoup
url = "https://444.hu/"
page = urlopen(url)
soup = BeautifulSoup(page,features='lxml')
page.close()




h1s = soup.find_all("h1")
for h1 in h1s:
    print(h1.a.text.strip())

