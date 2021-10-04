import sys
sys.path.insert(0, '/Users/kukak/IdeaProjects/untitled/src/test/coinmarket/src')

from main import KukaScrape

scrape = KukaScrape()

# Get the news
scrape.get_news()
