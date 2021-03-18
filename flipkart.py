import requests

from bs4 import BeautifulSoup

import csv

import re

base_url = "https://www.flipkart.com/search?q=mobiles&page="


def get_urls():
    with open("fliplart-data.csv", "a") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow(
            ['Product_name', 'Price', 'Rating', 'Product-url'])

        for page in range(1, 5):

            page = base_url + str(page)

            response = requests.get(page).text

            soup = BeautifulSoup(response, 'lxml')

            for product_urls in soup.find_all('a', href=True, attrs={'class': '_1fQZEK'}):
                name = product_urls.find('div', attrs={'class': '_4rR01T'}).text
                price = product_urls.find('div', attrs={'class': '_30jeq3 _1_WHN1'}).text
                rating = product_urls.find('div', attrs={'class': '_3LWZlK'}).text

                item_url = soup.find('a', class_="_1fQZEK", target="_blank")['href']

                item_url = " https://www.flipkart.com" + item_url

                item_url = re.split("\&", item_url)

                item_url = item_url[0]

                print(f'Product name is {name}')

                print(f'Product price is {price}')

                print(f'Product rating is {rating}')

                print(f'Product url is {item_url}')

                writer.writerow(
                    [name, price, rating, item_url])


get_urls()
