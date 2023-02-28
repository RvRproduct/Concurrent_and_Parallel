import multiprocessing as mp


def calc_square(numbers, result):
    for n in numbers:
        # result.append(n * n)
        result.put(n * n)

    print("inside process " + str(result))


if __name__ == "__main__":
    # manager method without while
    result = mp.Manager().list([])
    numbers = mp.Manager().list([2, 3, 5])
    result = mp.Queue()
    p = mp.Process(target=calc_square, args=([numbers, result]))

    p.start()
    p.join()

    while result.empty() is False:
        print(result.get())

    #print("outside process " + str(result))
