import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done Sleeping... {seconds}"


if __name__ == "__main__":

    # AS STARTED
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

        # AS COMPLETED
        # results = [executor.submit(do_something, sec) for sec in secs]

        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

        # f1 = executor.submit(do_something, 1)
        # f2 = executor.submit(do_something, 1)

        # print(f1.result())
        # print(f2.result())

    # processes = []

    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=[1.5])
    #     p.start()
    #     processes.append(p)

    # for process in processes:
    #     process.join()

    # p1 = multiprocessing.Process(target=do_something)
    # p2 = multiprocessing.Process(target=do_something)

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
