import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

soup = bs4.BeautifulSoup(res.text, 'lxml')

header_elems = soup.select('.mw-headline')

header_text = [item.getText() for item in header_elems]