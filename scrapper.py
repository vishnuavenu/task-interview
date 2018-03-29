from bs4 import BeautifulSoup
import requests
import sys
from product import Product
reload(sys)
sys.setdefaultencoding('utf8')


PAGE_TO_SCRAP = 'https://www.flipkart.com/mobiles/samsung~brand/pr?count=40&p%5B%5D=sort%3Drecency_desc&sid=tyy%2F4io&wid=1.productCard.PMU_V2'

SCRAPED_PRODUCT = []

# css classes for various component
PRODUCT_CARD = "_1UoZlX"
PRODUCT_SPECS = "tVe95H"
PRODUCT_NAME = "_3wU53n"

def main():

    # fetching the requested page for parsing
    r = requests.get(PAGE_TO_SCRAP)
    # print(r.text)
    if r.status_code != 200:
        print("[Error]: Unable to fetch the Page. Check Internet or proxy!")

    # creating soup = parsed html
    soup = BeautifulSoup( r.text,  'lxml')
    all_item_cards = soup.find_all("a", PRODUCT_CARD)
    for card in all_item_cards:
        specs_elem = card.find_all('li', { 'class': PRODUCT_SPECS})
        specs = [ spec.text for spec in specs_elem ]
        name = card.find('div', {'class': PRODUCT_NAME}).text
        product = Product(name, specs)
        SCRAPED_PRODUCT.append(product)
        print(" * "*12)

    # printing all data fetched for the page
    print(" Scrapped Product : ")
    for product in SCRAPED_PRODUCT:
        print("*"*20)
        print(product)
        print("*" * 20)

if __name__ == '__main__':
    main()