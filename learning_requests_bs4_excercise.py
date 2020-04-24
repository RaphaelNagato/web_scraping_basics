import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/w/index.php' + \
    '?title=List_Of_Game_of_Thrones_episodes&oldid=802553687'

r = requests.get(url)
html_contents = r.text  # get the text content of the response
# Parses the html markup using beautiful soup
html_soup = BeautifulSoup(html_contents, 'html.parser')

all_a_tags = html_soup.find_all('a')  # finds all a tags in the markup

links = []
for each_a_tag in all_a_tags:
    # for each a tag in the markup, it checks if there is a href attribute and if true, append to list
    if each_a_tag.get('href'):
        link = each_a_tag['href']
        links.append(link)
print(len(links))
