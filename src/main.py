import requests
from bs4 import BeautifulSoup

import json
from requests import Session, get
from requests.sessions import session
array = []


class KukaScrape:
    @staticmethod
    def get_link():
        url = f'https://coinmarketcap.com/all/views/all/'
        r = requests.get(url)
        bsoup = BeautifulSoup(r.text, 'html.parser')
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
            bsoup = BeautifulSoup (r.content, 'lxml')
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
        bsoup = BeautifulSoup (r.content, 'lxml')
        for i in range(1):

            rank = bsoup.find(class_="namePill namePillPrimary")
            price_value = bsoup.find(class_="priceValue")
            name = bsoup.find('h2', class_="sc-1q9q90x-0 jCInrl h1")
            stats = bsoup.find_all(class_="statsValue")
            procent = bsoup.find(class_="sc-15yy2pl-0 kAXKAX")
            print(
                f'{rank.text} {name.text} ----- {price_value.text} ----- {stats[0].text} ---- {stats[2].text} -----{procent.text}')

    # @staticmethod
    # def get_id(name):
        # KukaScrape.get_link()
        #name1 = name.lower()
       # url = f"https://coinmarketcap.com/currencies/{name1}/"
       # r = requests.get(url)
       # bsoup = bs(r.content, 'lxml')
        # for i in range(1):
          #  rank = bsoup.find(class_="namePill namePillPrimary")
        #a_string = rank.text
        #numbers = s = ''.join(x for x in a_string if x.isdigit())
       # return numbers

    @staticmethod
    def get_news():
        name = str(input("Coin name to output news:"))
        name1 = name.lower()
        id = KukaScrape.get_id(name1)
        url = f"https://api.coinmarketcap.com/content/v3/news?coins={id}&page=1&size=10000"
        news = requests.get(url).json()
        all_data = []
        for i in range(0, len(news['data'])):
            all_data.append({
                'Title': news['data'][i]['meta']['title'],
                'Main information': news['data'][i]['meta']['subtitle'],
                'URL the article': news['data'][i]['meta']['sourceUrl'],
            })
        print(all_data)

    def get_id(name1):
        headers = {
            'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': 'e56ccff7-2eb2-4b97-a591-f538736dfdbe',
        }
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parametrs = {
            'start': '1',
            'limit': '690',
            'convert': 'USD'
        }
        json = requests.get(url, params=parametrs, headers=headers).json()
        coins = json['data']
        for x in coins:
            if x['slug'] == name1:
                return x['id']



