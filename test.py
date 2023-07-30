from bs4 import BeautifulSoup
from requests import get

link = 'https://gg.deals/deals/?sort=price'

soup = BeautifulSoup(get(link).content, 'html.parser')