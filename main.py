import requests
from bs4 import BeautifulSoup

target_url = 'https://bitflyer.jp/?bf=hhbmzc42'

r = requests.get(target_url)

soup = BeautifulSoup(r.text "html.parser")

buy-price = soup.select("#bfPriceAsk_1")

print(buy-price)
