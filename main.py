from bs4 import BeautifulSoup
import requests

URL = 'https://barbora.lv/produkti/mandelu-dzeriens-bez-cukura-alpro-1-l'
page = requests.get(URL)
content = page.content

soup = BeautifulSoup(content, 'html.parser')

h3_tag = soup.find('h3', {"class": "b-product-info--info-3-title"})
h3_name = h3_tag.text

food_table = soup.find(class_="table table-striped table-condensed")

rows = food_table.findChildren(['tr'])

for row in rows:
    cells = row.findChildren('td', {"class": "b-text-right"})
    for cell in cells:
        value = cell.string
        print("The value in this cell is %s" % value)