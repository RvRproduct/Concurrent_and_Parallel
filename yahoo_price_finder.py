import time
from workers.wiki_worker import WikiWorker
from workers.yahoo_finance_workers import YahooFinancePriceWorker


def sleep_a_little(seconds):
    time.sleep(seconds)


def main():
    scraper_start_time = time.time()

    wiki_worker = WikiWorker()
    current_workers = []
    for symbol in wiki_worker.get_sp_500_companies():
        yahoo_finance_price_worker = YahooFinancePriceWorker(symbol=symbol)
        current_workers.append(yahoo_finance_price_worker)

    for i in range(len(current_workers)):
        current_workers[i].join()

    print("Extracting time took:",
          round(time.time() - scraper_start_time, 1))


if __name__ == "__main__":
    main()
