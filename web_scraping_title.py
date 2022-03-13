from matplotlib.pyplot import title
import requests
import bs4

res = requests.get("http://www.example.com")

soup = bs4.BeautifulSoup(res.text, 'lxml')

title_elem = soup.select('title')

text = title_elem[0].getText()

print(text)

