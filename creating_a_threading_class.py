import time
from workers.sleepy_workers import SleepyWorker
from workers.squared_sum_workers import SquaredSumWorker


# You can pass the dameon parameter if you wants since you have **kwargs


def sleep_a_little(seconds):
    time.sleep(seconds)


def main():
    calc_start_time = time.time()

    current_workers = []
    for i in range(5):
        maximum_value = (i + 1) * 1000000
        squaresumworker = SquaredSumWorker(n=maximum_value)
        current_workers.append(squaresumworker)

    for i in range(len(current_workers)):
        current_workers[i].join()

    print("Calculating sum of squares took:",
          round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()

    current_workers = []
    for seconds in range(1, 6):
        sleepyworker = SleepyWorker(seconds=seconds)
        current_workers.append(sleepyworker)

    for i in range(len(current_workers)):
        current_workers[i].join()

    print("Sleep took:", round(time.time() - sleep_start_time, 1))


if __name__ == "__main__":
    main()
