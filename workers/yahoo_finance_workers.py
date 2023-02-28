import threading
from bs4 import BeautifulSoup
import requests
from lxml import html
import time
import random
from locale import atof
# APPL


class YahooFinancePriceWorker(threading.Thread):
    def __init__(self, symbol, **kwargs):
        super(YahooFinancePriceWorker, self).__init__(**kwargs)
        self._symbol = symbol
        base_url = "https://finance.yahoo.com/quote/"
        self._url = f"{base_url}{self._symbol}"
        self.start()

    def run(self):
        time.sleep(30 * random.random())
        r = requests.get(self._url)
        if r.status_code != 200:
            return
        page_contents = html.fromstring(r.text)
        # float
        # replace(fixes the , stuff)
        price = float(page_contents.xpath(
            '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]')[0].text.replace(',', ''))
        print(price)


# '//*[@id="quote-header-info"]/div[3]'


# r = requests.get("https://finance.yahoo.com/quote/AAPL")
# soup = BeautifulSoup(r.text)
# print(soup.title)

# page_contents = html.fromstring(r.text)
# print(page_contents)
# print(page_contents.xpath(
#     '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]')[0].text)
