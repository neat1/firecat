# import libraries
import requests
from bs4 import BeautifulSoup

url = 'https://444.hu/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')


#print(soup.prettify())
x = soup.find_all('p')

#print(soup.find_all('p',id= 'second'))

#print(soup.find_all('p',class_='chorus'))
print(soup.find_all(id='third'))
