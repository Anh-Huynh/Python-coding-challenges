from matplotlib.pyplot import title
import requests
import bs4

based_url = 'http://books.toscrape.com/catalogue/page-{}.html'

two_star_titles = []

for i in range(1,50): 
    res = requests.get(based_url.format(i))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    products = soup.select('article.product_pod')
    two_stars_products = [product for product in products if product.select('.star-rating.Two')]
    for product in two_stars_products:
        two_star_titles.append(product.select('h3 > a')[0]['title']) 
        
print (two_star_titles)