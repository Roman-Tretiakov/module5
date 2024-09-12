from datetime import datetime
from threading import Thread
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, mode='w', encoding='utf-8') as file:
        for w in range(1, word_count + 1):
            file.write(f'Какое-то слово № {w}\n')
            sleep(0.1)

    print(f'Завершилась запись в файл {file_name}. ')


start_time = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = datetime.now()

print('Работа потоков', end_time - start_time)

start_time = datetime.now()

first_thr = Thread(target=write_words, args=(10, 'example5.txt'))
second_thr = Thread(target=write_words, args=(30, 'example6.txt'))
third_thr = Thread(target=write_words, args=(200, 'example7.txt'))
fourth_thr = Thread(target=write_words, args=(100, 'example8.txt'))

first_thr.start()
second_thr.start()
third_thr.start()
fourth_thr.start()

first_thr.join()
second_thr.join()
third_thr.join()
fourth_thr.join()

end_time = datetime.now()

print('Работа потоков', end_time - start_time)
