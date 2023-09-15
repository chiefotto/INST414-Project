import requests
from bs4 import BeautifulSoup
import pandas as pd
import regex
import matplotlib 
import matplotlib.pyplot as plt





URL = "https://www.supremecommunity.com/season/fall-winter2023/times/us/2023-08-17/"
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



df['Item Sellout time'] = df['Item Sellout time'].replace('[a-zA-Z]', '0', regex=True)

df["Item Sellout time"] = pd.to_numeric(df["Item Sellout time"])


first_30 = df.head(30)




# first_30.plot(x="Item Name", y=["Item Color and Size","Item Sellout time"])

# plt.show()

