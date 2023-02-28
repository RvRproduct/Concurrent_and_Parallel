import multiprocessing as mp


def calc_square(numbers, result, v):
    v.value = 5.67
    for index, n in enumerate(numbers):
        result[index] = n * n


if __name__ == "__main__":
    numbers = [2, 3, 5]
    result = mp.Array("i", 3)
    v = mp.Value("d", 0.0)
    p = mp.Process(target=calc_square, args=(numbers, result, v))

    p.start()
    p.join()

    print("outside process " + str(result[:]) + " value " + str(v.value))
