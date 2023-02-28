import threading
from bs4 import BeautifulSoup
import requests
from lxml import html
import time
import random
from locale import atof
# APPL


class YahooFinancePriceScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        super(YahooFinancePriceScheduler, self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start()

    def run(self):
        while True:
            val = self._input_queue.get()
            if val == "DONE":
                break

            yahoo_finance_price_worker = YahooFinancePriceWorker(symbol=val)
            price = yahoo_finance_price_worker.get_price()
            print(price)
            time.sleep(random.random())


class YahooFinancePriceWorker():
    def __init__(self, symbol, **kwargs):
        self._symbol = symbol
        base_url = "https://finance.yahoo.com/quote/"
        self._url = f"{base_url}{self._symbol}"

    def get_price(self):
        r = requests.get(self._url)
        if r.status_code != 200:
            return
        page_contents = html.fromstring(r.text)
        # float
        # replace(fixes the , stuff)
        price = float(page_contents.xpath(
            '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]')[0].text.replace(',', ''))
        return price
