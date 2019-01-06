from bs4 import BeautifulSoup
with open("ecologicalpyramid.html","r") as ecological_pyramid:
     soup = BeautifulSoup(ecological_pyramid,"lxml")
producer_entries = soup.find("ul")
#print(producer_entries.li.div.string)
#print(producer_entries)
#print(producer_entries.li)
#print(producer_entries.li.div.string)

tag_li = soup.find("li")


search_for_stringonly = soup.find(text="fox")

primary_consumers = soup.find(id="primaryconsumers")
#print(primary_consumers.li)

css_class = soup.find(attrs={'class':'primaryconsumerlist'})



all_tertiaryconsumers = soup.find_all(class_="tertiaryconsumerlist")
print(type(all_tertiaryconsumers))

for tertiaryconsumer in all_tertiaryconsumers:
  print(tertiaryconsumer.div.string)