"""
One can create a pool of preocesses which will carry out tasks submitted to
it with the Pool class.

A process pool object which controls a pool of worker processes to which
jobs can be submitted. It supports asynchronous results with timeouts and
callbacks and has a parallel map implementation.
"""
import os
import time
from multiprocessing import Pool
# os.cpu_count()


def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s


def sum_square_with_mp(numbers):
    start_time = time.time()
    p = Pool()
    result = p.map(sum_square, numbers)

    p.close()
    p.join()

    end_time = time.time() - start_time

    print(
        f"Processing {len(numbers)} numbers took {end_time} time using multiprocessing.")


def sum_square_no_mp(numbers):
    start_time = time.time()
    result = []
    for i in numbers:
        result.append(sum_square(i))
    end_time = time.time() - start_time

    print(
        f"Processing {len(numbers)} numbers took {end_time} time using serial processing.")


if __name__ == "__main__":
    numbers = range(10000)

    sum_square_with_mp(numbers)
    sum_square_no_mp(numbers)
