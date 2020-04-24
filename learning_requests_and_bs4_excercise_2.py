import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes"

r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

rating_tables = html_soup.find(
    'div', class_='mw-graph').find_next_sibling('table', class_='wikitable')

print(rating_tables.prettify())
