# Coinmarketcap_scrape_top

Python3 wrapper around the [CoinMarketCap](https://coinmarketcap.com//)

### Installation
Install my repoisitory 
```bash
git clone https://github.com/kuka666/coinmarket.git
cd coinmarket
pip install -r requirements.txt 
```

### Usage
```bash
First of all you should change the your path in test.py.In my instance:
```
```python
import sys
sys.path.insert(0, '/Users/kukak/IdeaProjects/untitled/src/test/coinmarket/src')
```


```bash
Then Import class:
```
```python
from main import KukaScrape
scrape = KukaScrape()
```

### Examples

Usage examples:
```python
# Get N top coin output:
>>> scrape.get_top()
Number to output top: *INPUT THE NUMBER*
RANK ***** NAME ******** PRICE ****** MARKET CAPITILIZATION ******* VOLUME 24h
Rank #1 BitcoinBTC ----- $42,991.36 ----- $809,541,002,182 ---- $30,977,310,681 
Rank #2 EthereumETH ----- $2,959.65 ----- $348,452,874,189 ---- $17,990,442,523 
Rank #3 TetherUSDT ----- $0.9999 ----- $68,464,000,917 ---- $67,954,055,735
Rank #4 CardanoADA ----- $2.08 ----- $66,694,449,015 ---- $2,833,016,161
Rank #5 Binance CoinBNB ----- $372.88 ----- $62,694,830,010 ---- $2,204,941,048
```

```python
# Get the news about coin:
>>> scrape.get_news()
Coin name to output news:*YOUR INPUT*(in my case: tether)
[{'Title': 'Biden administration wants stablecoin issuers to be regulated as banks - WSJ', 'Main information': 'The Biden administration seeks to impose tight bank-like regulations on issuers of stablecoins like Tether (USDT-USD) to avoid financial panics, the Wall Street Journal reports, citing people with knowledge on the matter. Stablecoins are digital currencies pegged to a sovereign c...', 'URL the article': 'https://seekingalpha.com/news/3747092-biden-administration-wants-stablecoin-issuers-to-be-regulated-as-banks-wsj?utm_source=coinmarketcap.com&utm_medium=referral'},
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
