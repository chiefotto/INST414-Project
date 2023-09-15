import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = "https://www.supremecommunity.com/season/fall-winter2023/times/us/"
page = requests.get(URL)

page.text

soup = BeautifulSoup(page.text,'html.parser')### full html page


seasonal_drops = soup.find_all(type="radio")### seasons


#seasonal menu 
supreme_seasonal = []
for season in seasonal_drops:
    supreme_seasonal.append((season.get('value')))

##supreme_seasonal = list of supreme seasons


def create_seasonal_links(links):
    base_url = 'https://www.supremecommunity.com/season'
    seasonal_links_formatted = []
    base_url +=links
    cleaned_url = base_url.replace('/season/season','/season')
    seasonal_links_formatted.append(cleaned_url)
    return seasonal_links_formatted


season_links = [create_seasonal_links(x) for x in supreme_seasonal]
#print((season_links[2]))

flat_list = [item for sublist in season_links for item in sublist]






def season_parser(season_link):
    new_page = requests.get(season_link)
    new_page.text
    new_soup = BeautifulSoup(new_page.text,'html.parser')
    weekly_links = new_soup.find_all('a',class_='week-item__title opener')
    return weekly_links
    

week_links = [season_parser(n) for n in flat_list]

flat_list_2 = [item for sublist in week_links for item in sublist]

all_supreme_weeks = []

for line in flat_list_2:
    x = line['href']
    all_supreme_weeks.append(x)



base_url_weekly = 'https://www.supremecommunity.com'


clean_links = []
for week in all_supreme_weeks:
    j = base_url_weekly+week
    clean_links.append(j)

##clean_links has all the links for every week in every season




for links in clean_links:
    URL = links
    page = requests.get(URL)

    page.text

    soup = BeautifulSoup(page.text,'html.parser')

    supreme_list= soup.find_all(attrs = {'class':['restocks-item__title', 'restocks-item__option', 'restocks-item__price']})


    supreme_items = []
    for product in supreme_list:
        supreme_items.append(product.get_text())
    
supreme_items2 = [line.replace('\n','') for line in supreme_items]

data = [supreme_items2[i:i+3] for i in range(0,len(supreme_items2),3)]

df = pd.DataFrame(data, columns=['Item Name', 'Item Color and Size', 'Item Sellout time'])

print(df)










