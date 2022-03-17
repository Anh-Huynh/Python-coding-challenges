import re
import requests
import bs4

homepage = 'http://quotes.toscrape.com/'
base_url = 'https://quotes.toscrape.com/page/{}'


# scrap the homepage
res = requests.get(homepage)
soup = bs4.BeautifulSoup(res.text, 'lxml')

authors = {author.get_text() for author in soup.select('.author')}
texts = [quote.get_text() for quote in soup.select('div.quote > span.text')]
top_ten_tags = [tag.text for tag in soup.select('.tag-item')]
print(top_ten_tags)

# scrap for all authors on the website
all_authors = set()
i=1
while True:
    res = requests.get(base_url.format(i))
    pattern = 'No quotes found!'
    if (re.search(pattern, res.text)):
        print(all_authors)
        break
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    for author in soup.select('.author'):
        all_authors.add(author.get_text())
    i+=1




