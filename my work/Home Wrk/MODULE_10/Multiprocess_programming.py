import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for name in filenames:
        read_info(name)
    end_time = time.time()
    print("Линейный вызов занял:", end_time - start_time, "секунд")

    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print("Многопроцессорный вызов занял:", end_time - start_time, "секунд")
