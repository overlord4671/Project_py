import time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for word in range(1, word_count + 1):
            file.write(f"Какое-то слово № {word}\n")
            time.sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")


start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end = time.time()
print(f"Всего затрачено времени: {end - start:.3f} секунд")

args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

start = time.time()
threads = []
for word_count, file_name in args:
    thread = Thread(target=write_words, args=(word_count, file_name))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
end = time.time()
print(f"Всего затрачено времени: {end - start:.3f} секунд")
