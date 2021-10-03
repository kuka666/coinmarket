import requests
from bs4 import BeautifulSoup as bs
import json
import numpy as np
import csv
array = []

class KukaScrape:
    @staticmethod
    def get_link():
        url = f'https://coinmarketcap.com/all/views/all/'
        r = requests.get(url)
        bsoup = bs(r.text, 'html.parser')
        main_info = bsoup.find("tbody")
        tr_info = main_info.find_all("tr")
        for col in tr_info:
            td_info = col.find_all("td")
            for item in td_info:
                all_links = item.find_all('a', class_="cmc-link")
                for links in all_links:
                    urls = links.get("href").replace("markets/", "")
                    array.append(urls)
    @staticmethod
    def get_top():
        KukaScrape.get_link()
        main = list(dict.fromkeys(array))
        top_to_see = int(input("Number to output top:"))
        print(f'RANK ***** NAME ******** PRICE ****** MARKET CAPITILIZATION ******* VOLUME 24h')
        for i in range(top_to_see):
            url = f"https://coinmarketcap.com{main[i]}"
            r = requests.get(url)
            bsoup = bs(r.content, 'lxml')
            for i in range(1):
                rank = bsoup.find(class_="namePill namePillPrimary")
                price_value = bsoup.find(class_="priceValue")
                name = bsoup.find('h2', class_="sc-1q9q90x-0 jCInrl h1")
                stats = bsoup.find_all(class_="statsValue")
                print(
                    f'{rank.text} {name.text} ----- {price_value.text} ----- {stats[0].text} ---- {stats[2].text} ')
    @staticmethod
    def get_coin_data():
        KukaScrape.get_link()
        name = str(input("Coin name to output data:"))
        name1 = name.lower()
        print(f'RANK ***** NAME ******** PRICE ****** MARKET CAPITILIZATION ******* VOLUME 24h********Procent')
        url = f"https://coinmarketcap.com/currencies/{name1}/"
        r = requests.get(url)
        bsoup = bs(r.content, 'lxml')
        for i in range(1):

            rank = bsoup.find(class_="namePill namePillPrimary")
            price_value = bsoup.find(class_="priceValue")
            name = bsoup.find('h2', class_="sc-1q9q90x-0 jCInrl h1")
            stats = bsoup.find_all(class_="statsValue")
            procent = bsoup.find(class_="sc-15yy2pl-0 kAXKAX")
            print(
                f'{rank.text} {name.text} ----- {price_value.text} ----- {stats[0].text} ---- {stats[2].text} -----{procent.text}')
    
