from urllib.request import urlopen

from bs4 import BeautifulSoup
url = "https://444.hu/"
page = urlopen(url)
soup = BeautifulSoup(page,features='lxml')
page.close()




'''h1s = soup.find_all("h1")
for h1 in h1s:
    print(h1.a.text.strip())'''

text = soup.find_all(class_="oversized")
for i in text:
    print(i.text)



all_tertiaryconsumers = soup.find_all(class_="tertiaryconsumerlist")
print(type(all_tertiaryconsumers))

for tertiaryconsumer in all_tertiaryconsumers:
  print(tertiaryconsumer.div.string)
