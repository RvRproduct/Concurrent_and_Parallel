from multiprocessing import Pool, cpu_count


def square(x):
    return x ** 2


def main():
    num_processes = 4
    comparison_list = [1, 2, 3]
    num_cpu_available = cpu_count()
    print("num_cpu_available:", num_cpu_available)
    num_cpu_to_use = max(1, cpu_count() - 1)
    print("Number of cpus being used:", num_cpu_to_use)

    with Pool(num_cpu_to_use) as mp_pool:
        result = mp_pool.map(square, comparison_list)
    print(result)


if __name__ == "__main__":
    main()
