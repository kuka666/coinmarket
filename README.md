# Coinmarketcap_scrape_top

Python3 wrapper around the [CoinMarketCap](https://coinmarketcap.com//)

### Installation
PyPI
```bash
pip install coinmarketcap_scrape_top
```
or from source
```bash
git clone https://github.com/kuka666/coinmarketcap_scrape_top.git
cd coinmarketcap_scrape_top
pip install -r requirements.txt 
```

### Usage

```python
from coinmarketcap_scrape_top import scrapper
scrape = scrapper()
```

### Examples

Usage examples:
```python
# Get N top coin output:
>>> cg.get_top()
Number to output top: *INPUT THE NUMBER*
RANK ***** NAME ******** PRICE ****** MARKET CAPITILIZATION ******* VOLUME 24h
Rank #1 BitcoinBTC ----- $42,991.36 ----- $809,541,002,182 ---- $30,977,310,681 
Rank #2 EthereumETH ----- $2,959.65 ----- $348,452,874,189 ---- $17,990,442,523 
Rank #3 TetherUSDT ----- $0.9999 ----- $68,464,000,917 ---- $67,954,055,735
Rank #4 CardanoADA ----- $2.08 ----- $66,694,449,015 ---- $2,833,016,161
Rank #5 Binance CoinBNB ----- $372.88 ----- $62,694,830,010 ---- $2,204,941,048
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
