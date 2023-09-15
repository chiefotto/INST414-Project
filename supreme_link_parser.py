import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = "https://www.supremecommunity.com/season/fall-winter2023/times/us/"
page = requests.get(URL)

page.text

soup = BeautifulSoup(page.text,'html.parser')



seasonal_drops = soup.find_all(type="radio")


#seasonal menu 
supreme_seasonal = []
for season in seasonal_drops:
    supreme_seasonal.append((season.get('value')))

# print(supreme_seasonal)

### weekly menu after season has been selected


# print(supreme_weekly)
base_url = 'https://www.supremecommunity.com/season'
print(supreme_seasonal)
seasonal_index_selection = (int(input("input desired season index-- remember python starts at 0 ")))
base_url+= supreme_seasonal[seasonal_index_selection]
cleaned_url = base_url.replace('/season/season','/season')

#### url working!!!
# new_URL = base_url
new_page = requests.get(cleaned_url)

new_page.text

new_soup = BeautifulSoup(new_page.text,'html.parser')

weekly_links = new_soup.find_all('a',class_='week-item__title opener')

supreme_weekly = []
for link in weekly_links:
    link_url = link['href']
    supreme_weekly.append(link_url)


base_url_weekly = 'https://www.supremecommunity.com'
print(supreme_weekly)
weekly_index_selection = (int(input('choose weekly index')))
base_url_weekly += supreme_weekly[weekly_index_selection]
base_url_weekly.replace('/season/season','/season')
cleaned_url_weekly = base_url_weekly.replace('/season/season','/season')



print(cleaned_url_weekly)
