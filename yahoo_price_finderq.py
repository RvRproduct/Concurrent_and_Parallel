import time
from workers.wiki_worker import WikiWorker
from workers.yahoo_finance_workersq import YahooFinancePriceScheduler
from multiprocessing import Queue


def main():
    symbol_queue = Queue()
    scraper_start_time = time.time()

    wiki_worker = WikiWorker()
    yahoo_finance_price_scheduler_threads = []
    num_yahoo_finance_price_workers = 4
    for i in range(num_yahoo_finance_price_workers):
        yahoo_finance_price_scheduler = YahooFinancePriceScheduler(
            input_queue=symbol_queue)
        yahoo_finance_price_scheduler_threads.append(
            yahoo_finance_price_scheduler)

    for symbol in wiki_worker.get_sp_500_companies():
        # print("Inserting Symbol:")
        symbol_queue.put(symbol)
        # time.sleep(10)

    for i in range(len(yahoo_finance_price_scheduler_threads)):
        symbol_queue.put("DONE")

    for i in range(len(yahoo_finance_price_scheduler_threads)):
        yahoo_finance_price_scheduler_threads[i].join()
    # print(symbol_queue)
    # print(symbol_queue.get())
    print("Extracting time took:",
          round(time.time() - scraper_start_time, 1))


if __name__ == "__main__":
    main()
