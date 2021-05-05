from bs4 import BeautifulSoup
import requests
import json
import csv
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



def getNutritionDataFromBarbora(Barbora_url):
    page = requests.get(Barbora_url)
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')

    # Finding name of the product
    title = soup.find('meta', {'name': 'og:title'})
    product_name = title['content'] if title else 'No meta title given'

    # Finding the full path of categories
    category_name_full_path = \
    json.loads(soup.find('div', {'class': 'b-product-info b-product--js-hook'})['data-b-for-cart'])[
        'category_name_full_path']

    # Finding values
    food_table = soup.find(class_="table table-striped table-condensed")
    rows = food_table.findChildren(['tr'])
    n_value = []
    for row in rows:
        values = row.findChildren('td', {"class": "b-text-right"})
        for value in values:
            n_value.append(value.string)

    return [product_name] + [category_name_full_path] + n_value

def writeBarboraDatatoFile(Barbora_list):
    with open('sample.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(Barbora_list)

def main():
    writeBarboraDatatoFile(getNutritionDataFromBarbora('https://barbora.lv/produkti/mandelu-dzeriens-bez-cukura-alpro-1-l'))

if __name__ == "__main__":
    main()

