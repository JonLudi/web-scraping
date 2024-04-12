import requests
from bs4 import BeautifulSoup

tuckahoe_scrape = requests.get("https://www.tuckahoeschools.org")
print(tuckahoe_scrape)
soup = BeautifulSoup(tuckahoe_scrape.text, "html.parser")
print(soup)
links = soup.find_all('a')

for link in links:
    href = link.get('href')
    if href:
        print(href)